pyinstaller.exe .\src\main.py `
    --onedir `
    --name obsidian-launcher `
    --add-data "src\resources;resources" `
    --windowed `
    --icon src\resources\obsidian-icon-windows.ico
