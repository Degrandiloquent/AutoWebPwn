#!/usr/bin/env python3
"""
AutoWebPwn Setup Script
Helps users configure the framework and set up legal test applications
"""

import os
import sys
import subprocess
import platform

def print_header():
    print("\n" + "="*70)
    print("  🛡️  AutoWebPwn - Penetration Testing Framework Setup")
    print("="*70)

def check_system():
    """Check system requirements"""
    print("\n📋 Checking system requirements...\n")
    
    # Python version
    py_version = sys.version_info
    print(f"✅ Python {py_version.major}.{py_version.minor}.{py_version.micro}")
    
    # OS
    print(f"✅ OS: {platform.system()}")
    
    # Docker
    try:
        result = subprocess.run(['docker', '--version'], 
                              capture_output=True, text=True)
        print(f"✅ Docker: {result.stdout.strip()}")
    except FileNotFoundError:
        print("⚠️  Docker not found - needed for vulnerable app setup")

def setup_venv():
    """Set up Python virtual environment"""
    print("\n📦 Setting up Python virtual environment...\n")
    
    venv_path = 'venv'
    
    if os.path.exists(venv_path):
        print(f"✅ Virtual environment already exists at {venv_path}")
        return True
    
    try:
        subprocess.run([sys.executable, '-m', 'venv', venv_path], check=True)
        print(f"✅ Virtual environment created at {venv_path}")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ Failed to create virtual environment")
        return False

def install_dependencies():
    """Install Python dependencies"""
    print("\n📚 Installing Python dependencies...\n")
    
    if platform.system() == 'Windows':
        python_exe = 'venv\\Scripts\\python.exe'
        pip_exe = 'venv\\Scripts\\pip.exe'
    else:
        python_exe = 'venv/bin/python'
        pip_exe = 'venv/bin/pip'
    
    if not os.path.exists(pip_exe):
        print("❌ Virtual environment not properly set up")
        return False
    
    try:
        # Upgrade pip
        subprocess.run([pip_exe, 'install', '--upgrade', 'pip'], check=True)
        print("✅ Updated pip")
        
        # Install requirements
        if os.path.exists('requirements.txt'):
            subprocess.run([pip_exe, 'install', '-r', 'requirements.txt'], 
                         check=True)
            print("✅ Installed all requirements")
            return True
        else:
            print("❌ requirements.txt not found")
            return False
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def setup_docker_apps():
    """Set up legal vulnerable applications with Docker"""
    print("\n🐳 Docker Vulnerable Applications\n")
    
    try:
        subprocess.run(['docker', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("⚠️  Docker is not installed or not in PATH")
        print("    Install Docker from https://www.docker.com/")
        return False
    
    print("Available options:")
    print("  1. Start all vulnerable apps (docker-compose)")
    print("  2. Start only DVWA")
    print("  3. Start only WebGoat")
    print("  4. Start only Juice Shop")
    print("  5. Skip Docker setup\n")
    
    choice = input("Select option (1-5): ").strip()
    
    if choice == '1':
        print("\n🚀 Starting all applications with docker-compose...\n")
        try:
            subprocess.run(['docker-compose', 'up', '-d'], check=True)
            print("✅ All applications started!")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to start applications")
            return False
    
    elif choice == '2':
        print("\n🚀 Starting DVWA...\n")
        try:
            subprocess.run([
                'docker', 'run', '-d', '-p', '80:80',
                'vulnerables/web-dvwa'
            ], check=True)
            print("✅ DVWA started at http://localhost/dvwa")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to start DVWA")
            return False
    
    elif choice == '3':
        print("\n🚀 Starting WebGoat...\n")
        try:
            subprocess.run([
                'docker', 'run', '-d', '-p', '8080:8080', '-p', '9090:9090',
                'webgoat/goatandwolf'
            ], check=True)
            print("✅ WebGoat started at http://localhost:8080/WebGoat")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to start WebGoat")
            return False
    
    elif choice == '4':
        print("\n🚀 Starting Juice Shop...\n")
        try:
            subprocess.run([
                'docker', 'run', '-d', '-p', '3000:3000',
                'bkimminich/juice-shop'
            ], check=True)
            print("✅ Juice Shop started at http://localhost:3000")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to start Juice Shop")
            return False
    
    else:
        print("⏭️  Skipping Docker setup")
        return True

def verify_installation():
    """Verify installation is complete"""
    print("\n✓ Verification\n")
    
    checks = {
        'main.py exists': os.path.exists('main.py'),
        'requirements.txt exists': os.path.exists('requirements.txt'),
        'config/config.yaml exists': os.path.exists('config/config.yaml'),
        'test_runner.py exists': os.path.exists('test_runner.py'),
        'TESTING_GUIDE.md exists': os.path.exists('TESTING_GUIDE.md'),
        'README.md exists': os.path.exists('README.md'),
    }
    
    all_ok = True
    for check, result in checks.items():
        symbol = "✅" if result else "❌"
        print(f"{symbol} {check}")
        if not result:
            all_ok = False
    
    return all_ok

def print_next_steps():
    """Print next steps for user"""
    print("\n" + "="*70)
    print("🎯 NEXT STEPS")
    print("="*70)
    
    print("\n1. Run a test scan:")
    if platform.system() == 'Windows':
        print("   venv\\Scripts\\python.exe main.py -u http://localhost/dvwa")
    else:
        print("   source venv/bin/activate")
        print("   python main.py -u http://localhost/dvwa")
    
    print("\n2. Use the test runner for batch testing:")
    if platform.system() == 'Windows':
        print("   venv\\Scripts\\python.exe test_runner.py all")
    else:
        print("   python test_runner.py all")
    
    print("\n3. Check the documentation:")
    print("   - README.md (overview and quick start)")
    print("   - TESTING_GUIDE.md (detailed setup and usage)")
    print("   - config/config.yaml (advanced configuration)")
    
    print("\n4. View scan results:")
    print("   - Check *.pdf files for vulnerability reports")
    print("   - Check logs/autowebpwn.log for detailed logs")
    
    print("\n" + "="*70)
    print("⚠️  REMEMBER: Only test authorized targets with written permission!")
    print("="*70 + "\n")

def main():
    print_header()
    
    # Check system
    check_system()
    
    # Set up Python environment
    if not setup_venv():
        print("\n❌ Setup failed during virtual environment creation")
        sys.exit(1)
    
    if not install_dependencies():
        print("\n❌ Setup failed during dependency installation")
        sys.exit(1)
    
    # Set up Docker applications
    setup_docker_apps()
    
    # Verify installation
    if not verify_installation():
        print("\n⚠️  Some files are missing - check your installation")
    
    # Print next steps
    print_next_steps()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Setup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
