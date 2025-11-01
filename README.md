# Clone the repository
git clone https://github.com/your-username/farmai-agricultural-app.git
cd farmai-agricultural-app

# Create project structure
mkdir -p backend/frontend/datasets/notebooks/docs/models

# Create initial files
touch backend/requirements.txt
touch backend/app.py
touch frontend/index.html
touch README.md

# Add initial content to README.md
echo "# FarmAI - Agricultural AI Assistant" > README.md
echo "## Team Members" >> README.md
echo "- Person A" >> README.md
echo "- Person B" >> README.md
echo "- Person C" >> README.md
echo "- Person D" >> README.md

# Initial commit
git add .
git commit -m "Initial commit: Project structure and setup"
git push origin main
