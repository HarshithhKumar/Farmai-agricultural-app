"""
Conservative fix for requirements.txt - Python 3.12 compatibility
Only updates packages that MUST be changed, keeps everything else the same
"""

# Minimal changes needed for Python 3.12
MUST_FIX = {
    'mediapipe==0.10.1': 'mediapipe==0.10.14',  # 0.10.1 not available for 3.12
}

# Lines to comment out (already installed or broken)
COMMENT_OUT = [
    'PyAudio @',  # Already removed/installed manually
    'pipwin',     # Broken on Python 3.12
]

# Packages that might fail but we'll try first
WATCH_LIST = [
    'tensorflow==2.12.0',
    'tensorflow-intel==2.12.0', 
    'tensorboard==2.12.3',
]

def fix_requirements(input_file='requirements.txt', output_file='requirements_py312.txt'):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_lines = []
    changes_made = []
    
    for line in lines:
        original_line = line
        line_stripped = line.strip()
        
        # Skip empty lines
        if not line_stripped:
            fixed_lines.append(line)
            continue
        
        # Check if should be commented out
        should_comment = False
        for pattern in COMMENT_OUT:
            if pattern in line_stripped:
                should_comment = True
                fixed_lines.append(f'# {line_stripped}  # Removed for Python 3.12\n')
                changes_made.append(f"Commented: {line_stripped[:50]}...")
                break
        
        if should_comment:
            continue
        
        # Check if needs fixing
        fixed = False
        for old_version, new_version in MUST_FIX.items():
            if old_version in line_stripped:
                fixed_lines.append(f'{new_version}\n')
                changes_made.append(f"{old_version} → {new_version}")
                fixed = True
                break
        
        if not fixed:
            # Check if on watch list
            for watch_pkg in WATCH_LIST:
                if watch_pkg in line_stripped:
                    fixed_lines.append(f'{line_stripped}  # May need updating if fails\n')
                    break
            else:
                fixed_lines.append(original_line)
    
    # Write fixed file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(fixed_lines)
    
    print(f"✓ Created {output_file}")
    print(f"\n{'='*60}")
    print("CHANGES MADE:")
    print('='*60)
    for change in changes_made:
        print(f"  • {change}")
    
    print(f"\n{'='*60}")
    print("PACKAGES TO WATCH (may fail on Python 3.12):")
    print('='*60)
    for pkg in WATCH_LIST:
        print(f"  ⚠️  {pkg}")
    
    print(f"\n{'='*60}")
    print("NEXT STEPS:")
    print('='*60)
    print(f"1. Review {output_file}")
    print(f"2. Run: pip install -r {output_file}")
    print("3. If TensorFlow fails, let me know and we'll fix it")
    print('='*60)

if __name__ == '__main__':
    fix_requirements()