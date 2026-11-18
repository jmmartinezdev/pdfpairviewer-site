# PDFPairViewer website

Static GitHub Pages website for PDFPairViewer. It includes a homepage, Privacy Policy, and Support page. No build tools, JavaScript, analytics, or cookies are added.

## Important: customize before publishing

Replace **all occurrences** of these placeholders:

- `José María Martínez Muñoz`: your legal name (privacy contact/controller identity).
- `support@jmmartinezdev.com`: your real support email address. The placeholders occur in both visible text and `mailto:` links.

Run the included script with Python 3 (no extra packages required):

```sh
python3 replace_placeholders.py --legal-name "Your Legal Name" --support-email "support@example.com"
```

The script updates UTF-8 text files throughout this project, including this README,
and escapes special characters in HTML files. It skips hidden files/directories,
binary files, symlinks, and its own source. Files are edited in place; keep a backup
or commit your changes first. You can run it from any directory using its full path.
Only placeholders are replaced; rerunning it does not change values already filled in.

Review the privacy policy against what your **release build** actually does, particularly local file handling, networking, analytics, crash diagnostics, retention of support messages, and any third-party dependencies. Update the policy if reality differs. Check whether additional business/legal notices are required for your circumstances in Spain or the EU. Keep your support email active.

## Structure

```
index.html          Homepage
privacy/index.html  Privacy Policy
support/index.html  Support
assets/styles.css   Shared styles
.nojekyll           Disable Jekyll processing
```

## Publish with GitHub Pages (branch deployment)

1. Create a **public**, empty GitHub repository named `pdfpairviewer-site` (do not initialize it with a README).
2. In a terminal, inside this folder:

   ```sh
   git init
   git branch -M main
   git add .
   git commit -m "Add PDFPairViewer website"
   git remote add origin https://github.com/USERNAME/pdfpairviewer-site.git
   git push -u origin main
   ```

3. On GitHub: Repository **Settings → Pages → Build and deployment**.
4. Choose **Deploy from a branch**, **main**, **/(root)**, and click **Save**.
5. Once deployed, the URLs will be:

   - `https://USERNAME.github.io/pdfpairviewer-site/`
   - `https://USERNAME.github.io/pdfpairviewer-site/privacy/`
   - `https://USERNAME.github.io/pdfpairviewer-site/support/`

Replace `USERNAME` with your real GitHub username. On GitHub Free, the repository must be public. The site itself is public.

## App Store Connect

- **App Privacy → Privacy Policy URL**: use the `/privacy/` URL.
- **App version → Support URL**: use the `/support/` URL.
- **Marketing URL** (optional): use the homepage.

GitHub Pages documentation:
https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site

Apple Support URL reference:
https://developer.apple.com/help/app-store-connect/reference/app-information/platform-version-information/

Apple privacy requirements:
https://developer.apple.com/help/app-store-connect/manage-app-information/manage-app-privacy
