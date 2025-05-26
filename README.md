# Hello World Jekyll Site

A simple Jekyll website for GitHub Pages with Tailwind CSS 4.x styling.

## Setup with asdf

This project uses asdf for tool management. Make sure you have asdf installed.

### 1. Install Ruby

```bash
# Install the Ruby version specified in .tool-versions
asdf install ruby

# Set the local Ruby version
asdf local ruby 3.2.1
```

### 2. Install Dependencies

```bash
# Install bundler
gem install bundler

# Install Jekyll and dependencies
bundle install
```

### 3. Run Locally

```bash
# Start the Jekyll development server
bundle exec jekyll serve

# Or with live reload
bundle exec jekyll serve --livereload
```

Visit `http://localhost:4000` to see your site.

## GitHub Pages Deployment

1. Push this repository to GitHub
2. Go to your repository settings
3. Navigate to "Pages" section
4. Set source to "Deploy from a branch"
5. Select "main" branch and "/ (root)" folder
6. Your site will be available at `https://yourusername.github.io/repository-name`

## File Structure

```
.
├── _config.yml          # Jekyll configuration
├── _layouts/            # HTML layouts
│   └── default.html     # Default page layout with Tailwind CSS
├── _site/               # Generated site (ignored by git)
├── .tool-versions       # asdf tool versions
├── Gemfile              # Ruby dependencies (includes webrick)
├── .gitignore           # Git ignore rules
├── index.md             # Homepage with Tailwind components
├── about.md             # About page with Tailwind styling
└── README.md            # This file
```

## Features

- **Jekyll 3.9.3**: GitHub Pages compatible static site generator
- **Tailwind CSS 4.x**: Latest version via CDN for modern styling
- **Responsive Design**: Mobile-first approach with Tailwind utilities
- **asdf Integration**: Ruby version management
- **GitHub Pages Ready**: Optimized for GitHub Pages deployment

## Customization

- Edit `_config.yml` to change site settings
- Modify `_layouts/default.html` to change the design and Tailwind classes
- Add new pages by creating `.md` files
- Use Tailwind CSS classes for styling - no custom CSS needed!
- Customize colors, spacing, and components using Tailwind utilities

## Learn More

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [asdf Documentation](https://asdf-vm.com/)
