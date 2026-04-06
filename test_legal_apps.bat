@echo off
REM AutoWebPwn - Legal Vulnerable Application Testing Batch Script for Windows

setlocal enabledelayedexpansion

title AutoWebPwn - Legal Vulnerable App Testing

echo.
echo ================================================================================
echo   AutoWebPwn - Legal Vulnerable Application Testing
echo ================================================================================
echo.
echo Choose an option:
echo.
echo   1. Start DVWA (Damn Vulnerable Web Application)
echo   2. Start WebGoat (OWASP Interactive Learning)
echo   3. Start bWAPP (Buggy Web Application)
echo   4. Start Juice Shop (OWASP Modern Vulnerable App)
echo   5. Start ALL vulnerable apps (requires docker-compose)
echo   6. Scan DVWA
echo   7. Scan WebGoat
echo   8. Scan bWAPP
echo   9. Scan Juice Shop
echo   10. Scan ALL apps
echo   0. Exit
echo.

set /p choice="Enter your choice (0-10): "

if "%choice%"=="1" (
    echo.
    echo Starting DVWA on http://localhost/dvwa ...
    docker run -d -p 80:80 vulnerables/web-dvwa
    echo DVWA started! Access at http://localhost/dvwa (admin/password)
    pause
    goto menu
)

if "%choice%"=="2" (
    echo.
    echo Starting WebGoat on http://localhost:8080/WebGoat ...
    docker run -d -p 8080:8080 -p 9090:9090 webgoat/goatandwolf
    echo WebGoat started! Access at http://localhost:8080/WebGoat
    pause
    goto menu
)

if "%choice%"=="3" (
    echo.
    echo Starting bWAPP on http://localhost/bWAPP ...
    docker run -d -p 80:80 raesene/bwapp
    echo bWAPP started! Access at http://localhost/bWAPP (bee/bug)
    pause
    goto menu
)

if "%choice%"=="4" (
    echo.
    echo Starting Juice Shop on http://localhost:3000 ...
    docker run -d -p 3000:3000 bkimminich/juice-shop
    echo Juice Shop started! Access at http://localhost:3000
    pause
    goto menu
)

if "%choice%"=="5" (
    echo.
    echo Starting ALL vulnerable apps with docker-compose...
    docker-compose up -d
    echo.
    echo All apps started!
    echo   - DVWA: http://localhost/dvwa (admin/password)
    echo   - WebGoat: http://localhost:8080/WebGoat
    echo   - bWAPP: http://localhost/bWAPP (bee/bug)
    echo   - Juice Shop: http://localhost:3000
    pause
    goto menu
)

if "%choice%"=="6" (
    echo.
    echo Scanning DVWA...
    venv\Scripts\python.exe main.py -u http://localhost/dvwa --cookie "security=low" -o report_dvwa.pdf
    echo.
    echo Scan complete! Report saved to report_dvwa.pdf
    pause
    goto menu
)

if "%choice%"=="7" (
    echo.
    echo Scanning WebGoat...
    venv\Scripts\python.exe main.py -u http://localhost:8080/WebGoat -o report_webgoat.pdf
    echo.
    echo Scan complete! Report saved to report_webgoat.pdf
    pause
    goto menu
)

if "%choice%"=="8" (
    echo.
    echo Scanning bWAPP...
    venv\Scripts\python.exe main.py -u http://localhost/bWAPP -o report_bwapp.pdf
    echo.
    echo Scan complete! Report saved to report_bwapp.pdf
    pause
    goto menu
)

if "%choice%"=="9" (
    echo.
    echo Scanning Juice Shop...
    venv\Scripts\python.exe main.py -u http://localhost:3000 -o report_juice_shop.pdf
    echo.
    echo Scan complete! Report saved to report_juice_shop.pdf
    pause
    goto menu
)

if "%choice%"=="10" (
    echo.
    echo Running all scans...
    venv\Scripts\python.exe test_runner.py all
    echo.
    echo All scans complete! Reports saved.
    pause
    goto menu
)

if "%choice%"=="0" (
    echo.
    echo Goodbye!
    exit /b 0
)

echo.
echo Invalid choice. Please try again.
pause

:menu
goto start

:start
cls
goto main
