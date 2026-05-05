# =====================================================
# ًںڑ€ HubSave - ط³ظƒط±ط¨طھ ط±ظپط¹ ط¥طµط¯ط§ط± ط¬ط¯ظٹط¯ ط¹ظ„ظ‰ GitHub
# =====================================================
# ظƒظٹظپظٹط© ط§ظ„ط§ط³طھط®ط¯ط§ظ…:
#   1. ط§ط¨ظ†ظگ APK ط§ظ„ط¬ط¯ظٹط¯ ظ…ظ† Android Studio (Build > Generate Signed APK)
#   2. ط§ظپطھط­ PowerShell ظپظٹ ظ…ط¬ظ„ط¯ ط§ظ„ظ…ط´ط±ظˆط¹
#   3. ط´ط؛ظ‘ظ„: .\upload-release.ps1
# =====================================================

# â”€â”€ ط¥ط¹ط¯ط§ط¯ط§طھ (ط؛ظٹظ‘ط± ظ‡ظ†ط§ ظپظ‚ط·) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
$GITHUB_TOKEN  = "YOUR_GITHUB_TOKEN_HERE"  # ط§ظ„طھظˆظƒظ†
$REPO_OWNER    = "uot2"                                         # ط§ط³ظ… ط­ط³ط§ط¨ظƒ
$REPO_NAME     = "HubSave-App"                                  # ط§ط³ظ… ط§ظ„ظ€ Repository
$APK_PATH      = "C:\Users\ط§ط¨ظˆ ط§ط³ط¯\OneDrive\Desktop\hack\app\build\outputs\apk\release\app-release.apk"
# â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

Write-Host ""
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host "   HubSave - ط±ظپط¹ ط¥طµط¯ط§ط± ط¬ط¯ظٹط¯" -ForegroundColor Cyan
Write-Host "=======================================" -ForegroundColor Cyan
Write-Host ""

# ط§ط³ط£ظ„ ط¹ظ† ط±ظ‚ظ… ط§ظ„ط¥طµط¯ط§ط±
$version = Read-Host "ًں”¢ ط£ط¯ط®ظ„ ط±ظ‚ظ… ط§ظ„ط¥طµط¯ط§ط± ط§ظ„ط¬ط¯ظٹط¯ (ظ…ط«ط§ظ„: v2.0)"
$releaseName = Read-Host "ًں“‌ ط£ط¯ط®ظ„ ط§ط³ظ… ط§ظ„ط¥طµط¯ط§ط± (ظ…ط«ط§ظ„: HubSave v2.0 - Bug Fixes)"
$releaseNotes = Read-Host "ًں“‹ ط£ط¯ط®ظ„ ظ…ظ„ط§ط­ط¸ط§طھ ط§ظ„ط¥طµط¯ط§ط± (ط§ط¶ط؛ط· Enter ظ„طھط®ط·ظٹ)"

if ([string]::IsNullOrEmpty($releaseNotes)) {
    $releaseNotes = "طھط­ط¯ظٹط« ط¬ط¯ظٹط¯ ظ„ظ€ HubSave $version"
}

# طھط­ظ‚ظ‚ ظ…ظ† ظˆط¬ظˆط¯ ظ…ظ„ظپ APK
if (-not (Test-Path $APK_PATH)) {
    Write-Host ""
    Write-Host "â‌Œ ط®ط·ط£: ظ„ظ… ظٹطھظ… ط§ظ„ط¹ط«ظˆط± ط¹ظ„ظ‰ ظ…ظ„ظپ APK ظپظٹ ط§ظ„ظ…ط³ط§ط±:" -ForegroundColor Red
    Write-Host "   $APK_PATH" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "طھط£ظƒط¯ ظ…ظ† ط¨ظ†ط§ط، ط§ظ„طھط·ط¨ظٹظ‚ ط£ظˆظ„ط§ظ‹ ظ…ظ† Android Studio:" -ForegroundColor Yellow
    Write-Host "   Build > Generate Signed Bundle / APK > APK > Release" -ForegroundColor Yellow
    exit 1
}

$apkSize = [math]::Round((Get-Item $APK_PATH).Length / 1MB, 1)
Write-Host ""
Write-Host "âœ… ظ…ظ„ظپ APK ظ…ظˆط¬ظˆط¯ ($apkSize MB)" -ForegroundColor Green
Write-Host ""
Write-Host "ط³ظٹطھظ… ط±ظپط¹ ط§ظ„ط¥طµط¯ط§ط± ط§ظ„طھط§ظ„ظٹ:" -ForegroundColor White
Write-Host "   Tag:     $version" -ForegroundColor Cyan
Write-Host "   Name:    $releaseName" -ForegroundColor Cyan
Write-Host "   APK:     HubSave-pro.apk ($apkSize MB)" -ForegroundColor Cyan
Write-Host ""

$confirm = Read-Host "ظ‡ظ„ طھط±ظٹط¯ ط§ظ„ظ…طھط§ط¨ط¹ط©طں (y/n)"
if ($confirm -ne "y" -and $confirm -ne "Y" -and $confirm -ne "yes") {
    Write-Host "طھظ… ط§ظ„ط¥ظ„ط؛ط§ط،." -ForegroundColor Yellow
    exit 0
}

# ط§ظ„ط®ط·ظˆط© 1: ط¥ظ†ط´ط§ط، ط§ظ„ظ€ Release
Write-Host ""
Write-Host "âڈ³ ط§ظ„ط®ط·ظˆط© 1/2: ط¥ظ†ط´ط§ط، Release ط¹ظ„ظ‰ GitHub..." -ForegroundColor Yellow

$headers = @{
    Authorization = "token $GITHUB_TOKEN"
    Accept        = "application/vnd.github+json"
}

$releaseBody = @{
    tag_name   = $version
    name       = $releaseName
    body       = $releaseNotes
    draft      = $false
    prerelease = $false
} | ConvertTo-Json

try {
    $release = Invoke-RestMethod `
        -Uri "https://api.github.com/repos/$REPO_OWNER/$REPO_NAME/releases" `
        -Method POST `
        -Headers $headers `
        -Body $releaseBody `
        -ContentType "application/json"
    
    Write-Host "âœ… طھظ… ط¥ظ†ط´ط§ط، Release ط¨ظ†ط¬ط§ط­! (ID: $($release.id))" -ForegroundColor Green
} catch {
    Write-Host "â‌Œ ظپط´ظ„ ط¥ظ†ط´ط§ط، Release: $_" -ForegroundColor Red
    exit 1
}

# ط§ظ„ط®ط·ظˆط© 2: ط±ظپط¹ ظ…ظ„ظپ APK
Write-Host ""
Write-Host "âڈ³ ط§ظ„ط®ط·ظˆط© 2/2: ط±ظپط¹ ظ…ظ„ظپ APK ($apkSize MB)... ظ‚ط¯ ظٹط³طھط؛ط±ظ‚ ط¯ظ‚ظٹظ‚ط©" -ForegroundColor Yellow

$uploadUrl = "https://uploads.github.com/repos/$REPO_OWNER/$REPO_NAME/releases/$($release.id)/assets?name=HubSave-pro.apk"
$uploadHeaders = @{
    Authorization  = "token $GITHUB_TOKEN"
    "Content-Type" = "application/octet-stream"
}

$apkBytes = [System.IO.File]::ReadAllBytes($APK_PATH)

try {
    $asset = Invoke-RestMethod `
        -Uri $uploadUrl `
        -Method POST `
        -Headers $uploadHeaders `
        -Body $apkBytes
    
    Write-Host "âœ… طھظ… ط±ظپط¹ APK ط¨ظ†ط¬ط§ط­!" -ForegroundColor Green
} catch {
    Write-Host "â‌Œ ظپط´ظ„ ط±ظپط¹ APK: $_" -ForegroundColor Red
    exit 1
}

# ط§ظ„ظ†طھظٹط¬ط© ط§ظ„ظ†ظ‡ط§ط¦ظٹط©
Write-Host ""
Write-Host "=======================================" -ForegroundColor Green
Write-Host "   ًںژ‰ طھظ… ط¨ظ†ط¬ط§ط­! " -ForegroundColor Green
Write-Host "=======================================" -ForegroundColor Green
Write-Host ""
Write-Host "ًں“¦ ط§ظ„ط¥طµط¯ط§ط±:  $version" -ForegroundColor White
Write-Host "ًں”— ط±ط§ط¨ط· ط§ظ„طھط­ظ…ظٹظ„ ط§ظ„ظ…ط¨ط§ط´ط±:" -ForegroundColor White
Write-Host "   https://github.com/$REPO_OWNER/$REPO_NAME/releases/download/$version/HubSave-pro.apk" -ForegroundColor Cyan
Write-Host ""
Write-Host "ًںŒگ ط²ط± ط§ظ„طھط­ظ…ظٹظ„ ظپظٹ ظ…ظˆظ‚ط¹ظƒ طھظ„ظ‚ط§ط¦ظٹط§ظ‹ ظٹط­ظ…ظ‘ظ„ ط§ظ„ظ†ط³ط®ط© ط§ظ„ط¬ط¯ظٹط¯ط© ط§ظ„ط¢ظ†:" -ForegroundColor White
Write-Host "   https://uot2.github.io/HubSave-App/" -ForegroundColor Cyan
Write-Host ""
Write-Host "ًں“ٹ ط´ط§ظ‡ط¯ ط¬ظ…ظٹط¹ ط§ظ„ط¥طµط¯ط§ط±ط§طھ:" -ForegroundColor White
Write-Host "   https://github.com/$REPO_OWNER/$REPO_NAME/releases" -ForegroundColor Cyan
Write-Host ""

