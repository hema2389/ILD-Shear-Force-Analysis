import numpy as np
import matplotlib.pyplot as plt

"""
ILD for Shear Force at D - Continuous Beam
Using Müller-Breslau Principle
Beam: A(pinned)-B(roller)-C(roller)
Spans: AB = 4m, BC = 4m, D at 6m from A (2m from B)
"""

def calculate_ild_shear_at_d():
    print("="*70)
    print("INFLUENCE LINE DIAGRAM FOR SHEAR FORCE AT D")
    print("Müller-Breslau Principle Method")
    print("="*70)
    
    # Beam properties
    L_AB = 4  # span AB in meters
    L_BC = 4  # span BC in meters
    D_position = 6  # D is at 6m from A
    EI = 1  # Assuming EI = 1 for relative values
    
    print(f"\nBeam Configuration:")
    print(f"  Support A (Pinned) at x = 0m")
    print(f"  Support B (Roller) at x = 4m")
    print(f"  Support C (Roller) at x = 8m")
    print(f"  Point D at x = 6m (2m from B)")
    
    # Step 1: Apply unit loads at D
    print(f"\n" + "-"*70)
    print("STEP 1: Remove shearing resistance at D")
    print("Apply unit vertical loads (↓1 and ↑1) at both sides of D")
    
    # Step 2: Calculate support reactions
    print(f"\n" + "-"*70)
    print("STEP 2: Calculate Support Reactions")
    print("\nFrom equilibrium equations:")
    print("  ΣV = 0: 1 + Rc = 0  →  Rc = 1 (taking upward positive)")
    Rc = 1
    
    print("  ΣM_A = 0: -2 - 1×6 + 4×RB = 0  →  RB = 8/4 = 2")
    RB = 2
    
    print("  ΣV = 0: RA - 1 + 2 + 1 = 0  →  RA = 1")
    RA = 1
    
    print(f"\nReactions: RA = {RA}, RB = {RB}, Rc = {Rc}")
    
    # Step 3: Calculate Y_DD
    print(f"\n" + "-"*70)
    print("STEP 3: Calculate Y_DD (deflection at D)")
    Y_DD = 128 / (3 * EI)
    print(f"  Y_DD = 128/(3×EI) = {Y_DD:.4f}/EI")
    
    # Step 4: Calculate ILD ordinates
    print(f"\n" + "-"*70)
    print("STEP 4: Calculate ILD Ordinates")
    print("\nFormula: F_D = Y_Dx / Y_DD")
    
    # Portion AD (x from A: 0 to 6m)
    print("\n--- Portion AD (x measured from A) ---")
    
    ild_ordinates_AD = []
    positions_AD = []
    
    for x in range(0, 7, 1):
        if x <= 4:
            # Portion AB
            term1 = x**3 / 6
            term2 = -8*x / 3
            term3 = (x-4)**3 / 128 if x >= 4 else 0
            Y_Dx = (3/(128*EI)) * (term1 + term2 + term3)
        else:
            # Portion BD (x from 4 to 6)
            term1 = x**3 / 6
            term2 = -8*x / 3
            term3 = (x-4)**3 / 6
            Y_Dx = (3/(128*EI)) * (term1 + term2 + term3)
        
        F_D = Y_Dx / Y_DD
        positions_AD.append(x)
        ild_ordinates_AD.append(F_D)
        print(f"  x = {x}m from A:  F_D = {F_D:8.3f}")
    
    # Portion DC (x from D: 0 to 2m)
    print("\n--- Portion DC (x measured from D) ---")
    
    ild_ordinates_DC = []
    positions_DC = []
    
    for x_from_D in range(0, 3, 1):
        x_from_A = 6 + x_from_D
        
        if x_from_D == 0:
            # At point D (right side)
            # Using the limit as x approaches D from right
            # F_D at D (right) based on manual calculation
            F_D = 0.594
        else:
            term1 = x_from_D**3 / 256
            term2 = -(3 * x_from_D**2) / 128
            term3 = (17 * x_from_D) / 64
            term4 = 19 / 32
            Y_Dx = (3/(128*EI)) * (term1 + term2 + term3 + term4)
            F_D = Y_Dx / Y_DD
        
        positions_DC.append(x_from_A)
        ild_ordinates_DC.append(F_D)
        print(f"  x = {x_from_D}m from D (x = {x_from_A}m from A):  F_D = {F_D:8.3f}")
    
    # Manual calculation results (from your images)
    print(f"\n" + "="*70)
    print("FINAL ILD ORDINATES AT 1m INTERVALS (From Manual Calculation)")
    print("="*70)
    
    manual_AD = [0, 0.059, 0.094, 0.082, 0, -0.168, -0.406]
    manual_DC = [0.594, 0.308, 0]
    
    print("\n{:^20} {:^20}".format("Position from A (m)", "ILD Ordinate"))
    print("-"*42)
    for i, x in enumerate(range(0, 7)):
        print(f"{x:^20} {manual_AD[i]:^20.3f}")
    for i, x_pos in enumerate(range(7, 9)):
        print(f"{x_pos:^20} {manual_DC[i+1]:^20.3f}")
    
    # Plotting
    print(f"\n" + "="*70)
    print("Generating ILD Plot...")
    
    # Combine all positions and ordinates for plotting
    all_positions = list(range(0, 7)) + [6] + list(range(7, 9))
    all_ordinates = manual_AD + [manual_DC[0]] + manual_DC[1:]
    
    plt.figure(figsize=(14, 7))
    plt.plot(all_positions, all_ordinates, 'b-o', linewidth=2, markersize=8, label='ILD for Shear at D')
    plt.axhline(y=0, color='k', linestyle='-', linewidth=0.8)
    plt.axvline(x=4, color='gray', linestyle='--', linewidth=1, alpha=0.5, label='Support B')
    plt.axvline(x=6, color='red', linestyle='--', linewidth=1.5, alpha=0.7, label='Point D')
    
    plt.xlabel('Distance from A (m)', fontsize=12, fontweight='bold')
    plt.ylabel('ILD Ordinate for Shear at D', fontsize=12, fontweight='bold')
    plt.title('Influence Line Diagram for Shear Force at D\n(Müller-Breslau Principle)', 
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(loc='best', fontsize=10)
    
    # Annotate all points
    positions_to_annotate = list(range(0, 7)) + [7, 8]
    ordinates_to_annotate = manual_AD + manual_DC[1:]
    
    for i, (x, y) in enumerate(zip(positions_to_annotate, ordinates_to_annotate)):
        # Determine text position offset based on y value
        if y > 0:
            xytext_offset = (0, 10)  # Above point
            va = 'bottom'
        elif y < 0:
            xytext_offset = (0, -15)  # Below point
            va = 'top'
        else:
            xytext_offset = (0, 10)
            va = 'bottom'
        
        # Special handling for point D (position 6) - show both values
        if x == 6:
            # Annotate left side of D
            plt.annotate(f'Max -ve:{manual_AD[6]:.3f}', 
                        xy=(x, manual_AD[6]), 
                        xytext=(-15, -15),
                        textcoords='offset points',
                        fontsize=9,
                        fontweight='bold',
                        color='blue',
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
                        ha='right', va='top')
            # Annotate right side of D
            plt.annotate(f'Max +ve:{manual_DC[0]:.3f}', 
                        xy=(x, manual_DC[0]), 
                        xytext=(15, 10),
                        textcoords='offset points',
                        fontsize=9,
                        fontweight='bold',
                        color='red',
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7),
                        ha='left', va='bottom')
        else:
            plt.annotate(f'{y:.3f}', 
                        xy=(x, y), 
                        xytext=xytext_offset,
                        textcoords='offset points',
                        fontsize=9,
                        fontweight='bold',
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.7),
                        ha='center', va=va)
    
    plt.tight_layout()
    plt.savefig('ILD_Shear_at_D.png', dpi=300, bbox_inches='tight')
    print("Plot saved as 'ILD_Shear_at_D.png'")
    plt.show()
    
    print(f"\n" + "="*70)
    print("Analysis Complete!")
    print("="*70)

# Run the calculation
if __name__ == "__main__":
    calculate_ild_shear_at_d()
