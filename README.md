# Continuous Integration using GitHub Actions of Python Data Science Project

![Testing](https://github.com/nogibjj/ids706-individual-project-1/actions/workflows/tests.yml/badge.svg)
![Formatting](https://github.com/nogibjj/ids706-individual-project-1/actions/workflows/format.yml/badge.svg)
![Linting](https://github.com/nogibjj/ids706-individual-project-1/actions/workflows/lint.yml/badge.svg)
![Installing](https://github.com/nogibjj/ids706-individual-project-1/actions/workflows/install.yml/badge.svg)

This is the "Continuous Integration using GitHub Actions of Python Data Science Project". The project utilizes GitHub Actions for Continuous Integration and provides a **.devcontainer** setup for seamless development inside a Docker container with Visual Studio Code.
 
## 🚀 Getting Started
### Local Development with VS Code and .devcontainer
1. Ensure you have **Docker** installed and running on your machine.
2. Install the **Remote - Containers** extension in VS Code.
3. Clone the repository onto your local machine.
4. Open the repository in VS Code.
5. A notification will pop up suggesting you reopen the project in a container. Click on "Reopen in Container". (Alternatively, you can press **F1**, type "Remote-Containers: Reopen Folder in Container", and press Enter.)
6. The first time you do this, Docker will build an image based on the provided **Dockerfile**. This may take a few minutes.
7. Once inside the container, you'll have a ready-to-use Python environment, isolated from your local system.

### 🧪 Running Tests

To run tests in this project, use the following command:

```bash
make test
```

This command runs all unit tests, including tests on the Jupyter notebook, script, and lib file, and ensures that any changes made haven't introduced new issues.

🛠️ File Structure
* polars.ipynb: A Jupyter Notebook containing cells that perform descriptive statistics using Polars.
* polars.py: A Python script performing the same descriptive statistics as the notebook.
* lib.py: A file that shares common code between the script and notebook.
* Makefile: Contains commands to run tests, format code, lint code, and install necessary Python packages.
* test_polars.py: Holds unit tests for the script.
* test_lib.py: Holds unit tests for the lib file.
* requirements.txt: Specifies the Python dependencies required for this project.
* .devcontainer: Configurations for the VS Code remote container development environment.
* .github/workflows: Workflow definitions for Continuous Integration using GitHub Actions.

✨ Contributing
1. Fork the repository.
2. Create a new branch for your contributions.
3. Implement your changes.
4. Run tests using the Makefile to ensure no new bugs have been introduced.
5. Submit a pull request detailing your changes.

*_This README provides an overview of the project, guides on the .devcontainer usage, instructions on running tests, file structure and outlines the contribution process. Modify or expand sections as needed for your project's specific requirements._*
