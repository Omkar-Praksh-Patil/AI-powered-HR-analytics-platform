# Contributing to Inventeron

Thank you for considering contributing to Inventeron! 🎉

## How to Contribute

### Reporting Bugs
1. Check if the issue already exists in [Issues](../../issues)
2. Open a new issue with:
   - A clear title
   - Steps to reproduce
   - Expected vs actual behavior
   - Screenshots (if applicable)

### Submitting Changes

1. **Fork** the repository
2. **Create a branch** for your feature:
   ```bash
   git checkout -b feat/your-feature-name
   ```
3. **Make your changes** with clear, descriptive commits
4. **Test** your changes locally
5. **Push** your branch and open a **Pull Request**

### Commit Message Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Use for |
|--------|---------|
| `feat:` | New features |
| `fix:` | Bug fixes |
| `docs:` | Documentation changes |
| `style:` | CSS/formatting changes |
| `refactor:` | Code refactoring |
| `chore:` | Build process, config changes |

### Code Style
- Follow PEP 8 for Python code
- Keep functions small and focused
- Add comments for complex logic

### Setting Up Dev Environment

```bash
git clone https://github.com/YOUR_USERNAME/inventeron.git
cd inventeron
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python clean_data.py
python train_model.py
python app.py
```

## Questions?

Open an issue with the label `question` and we'll get back to you!
