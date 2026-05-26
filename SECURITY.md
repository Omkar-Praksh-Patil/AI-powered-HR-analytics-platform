# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅ Yes    |

## Reporting a Vulnerability

If you discover a security vulnerability in Inventeron, please:

1. **Do NOT** open a public GitHub issue.
2. Email the details to: `omkar@inventeron.dev`
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact

We will respond within **48 hours** and aim to resolve critical vulnerabilities within **7 days**.

## Security Best Practices for Deployment

- Never commit `.env` files with real credentials
- Always set `FLASK_DEBUG=False` in production
- Use a strong, random `FLASK_SECRET_KEY`
- Restrict MongoDB access with authentication
- Run the app behind a reverse proxy (nginx) in production
