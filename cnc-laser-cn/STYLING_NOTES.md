# CNC-Laser Site - Fresh Styling Implementation

## Overview
This document describes the fresh visual system implemented for the cnc-laser-cn website.

## Color Palette

### Primary Brand Colors (Red)
- Primary Red: `#d32f2f`
- Primary Red Dark: `#b71c1c`
- Primary Red Light: `#ef5350`
- Primary Red Pale: `#ffebee`

### Graphite Scale (Neutral Colors)
- Graphite 900: `#1a1a1a` (darkest text)
- Graphite 800: `#2d2d2d` (dark backgrounds)
- Graphite 700: `#424242` (body text)
- Graphite 600: `#616161` (secondary text)
- Graphite 400: `#9e9e9e` (borders, disabled)
- Graphite 200: `#e0e0e0` (light borders)
- Graphite 100: `#f5f5f5` (light backgrounds)
- Graphite 50: `#fafafa` (very light backgrounds)

### White & Utilities
- White: `#ffffff`
- Light gray: `#f8f9fa`
- Medium gray: `#e9ecef`

## Typography

### Font Family
- Primary: `-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif`

### Heading Sizes
- H1: 3rem (3.5rem on hero)
- H2: 2.25rem
- H3: 1.75rem
- H4: 1.25rem
- H5: 1.125rem
- H6: 1rem (600 weight)

### Line Heights
- Headers: 1.2
- Body text: 1.6-1.7
- Paragraphs: 1.7

## Spacing System

Consistent spacing scale used throughout:
- xs: 0.25rem
- sm: 0.5rem
- md: 1rem
- lg: 1.5rem
- xl: 2rem
- 2xl: 3rem
- 3xl: 4rem
- 4xl: 6rem

## Components

### Navigation (.site-header)
- Sticky positioning
- Clean white background
- Red underline on active/hover states
- Responsive mobile menu with hamburger

### Hero Section
- Red gradient background: `linear-gradient(135deg, var(--primary-red) 0%, var(--primary-red-dark) 100%)`
- Desktop minimum height: 600px
- Responsive at all breakpoints down to 360px
- Content grid: 2 columns on desktop, 1 on mobile

### Cards
Available card types:
- `.feature-card` - Feature highlights with icons
- `.category-card` - Product categories
- `.product-card` - Individual products with specs
- `.value-card` - Company values
- `.support-card` - Support services

All cards feature:
- White background with subtle border
- Hover effect: translateY(-6px) + enhanced shadow
- Border highlights in red on hover
- Responsive grid layouts

### Tables
- `.specs-table` - Technical specifications
- `.comparison-table` - Product comparison

Features:
- Red gradient header background
- Row hover states (light red background)
- Responsive scroll on mobile
- Proper border styling

### Buttons
Button variants:
- `.btn-primary` - Red background, white text (main action)
- `.btn-secondary` - Graphite background
- `.btn-outline` - Red border, transparent background
- `.btn-ghost` - Minimal style with border

Sizes:
- Default: 0.875rem padding, 1rem font
- `.btn-sm`: Smaller
- `.btn-lg`: Larger

States:
- Hover: Color change + shadow enhancement
- Active: Scale animation
- Disabled: Reduced opacity

### Forms
- Clean input styling with borders
- Focus state: Red border + light red shadow
- Label styling with proper weight
- Full-width text areas with min-height

### Footer
- Dark graphite background (#1a1a1a)
- Responsive grid layout
- Social link circles with hover effects
- Proper link colors and hover states

## Grid Utilities

### Layout Grids
- `.features-grid` - auto-fit, minmax(280px, 1fr)
- `.categories-grid` - auto-fit, minmax(320px, 1fr)
- `.products-grid` - auto-fit, minmax(360px, 1fr)
- `.support-grid` - auto-fit, minmax(280px, 1fr)

### Flex Utilities
- `.flex` - display: flex
- `.flex-col` - flex-direction: column
- `.flex-center` - center content
- `.flex-between` - space-between + center

### Margin/Padding Classes
- `.mb-*` `.mt-*` - Margin utilities
- `.mb-0`, `.mb-sm`, `.mb-md`, `.mb-lg`, `.mb-xl`
- `.p-md`, `.p-lg`, `.px-lg`, `.py-lg`

## Responsive Breakpoints

### Desktop (1200px max-width container)
- Full multi-column layouts
- Standard padding and spacing
- All hover effects active

### Tablet (max-width: 1024px)
- Adjusted heading sizes
- Hero content switches to single column
- Grid adjustments for medium screens

### Mobile (max-width: 768px)
- Mobile hamburger menu
- Single column layouts for grids
- Adjusted typography
- Flexible button layouts

### Small Mobile (max-width: 480px)
- Further spacing adjustments
- Optimized font sizes
- Full-width buttons
- Compact card padding

### Extra Small (max-width: 360px)
- Minimum viable display
- Tight spacing
- Very small fonts
- Optimized for narrow screens

## Transitions & Effects

### Animation Timing
- Fast: 150ms cubic-bezier(0.4, 0, 0.2, 1)
- Normal: 300ms cubic-bezier(0.4, 0, 0.2, 1)
- Slow: 500ms cubic-bezier(0.4, 0, 0.2, 1)

### Common Effects
- Hover: Color change + shadow enhancement
- Button active: Scale(0.98)
- Card hover: TranslateY(-6px)
- Image hover: Scale(1.05)
- Menu animation: Smooth transform

## Shadows

Professional shadow system:
- `--shadow-sm`: 0 1px 3px rgba(0, 0, 0, 0.08)
- `--shadow-md`: 0 4px 12px rgba(0, 0, 0, 0.1)
- `--shadow-lg`: 0 10px 24px rgba(0, 0, 0, 0.12)
- `--shadow-xl`: 0 20px 40px rgba(0, 0, 0, 0.15)

## Border Radius

Consistent rounding:
- sm: 4px
- md: 8px
- lg: 12px
- xl: 16px

## Implementation Details

### Semantic Classes
All HTML uses semantic class names:
- Navigation: `.site-header`, `.main-nav`, `.nav-menu`, `.dropdown`
- Content: `.container`, `.section-title`, `.breadcrumb`
- Sections: `.hero`, `.page-header`, `.cta`, `.site-footer`

### No Inline Styles
All styling is in CSS variables and classes. No inline style attributes.

### No External Dependencies
Pure CSS styling - no external libraries required.

### Consistency
All pages share the same stylesheet:
- `assets/css/main.css` - Core styles (1260 lines)
- `assets/css/components.css` - Component-specific styles (1143 lines)

## CSS Variables Reference

All colors, spacing, and effects use CSS variables defined in `:root`:
```css
--primary-red: #d32f2f;
--graphite-900: #1a1a1a;
--spacing-lg: 1.5rem;
--shadow-md: 0 4px 12px rgba(0, 0, 0, 0.1);
--radius-md: 8px;
--transition-normal: 300ms cubic-bezier(0.4, 0, 0.2, 1);
```

Easy to update globally by modifying `:root` values.

## Browser Support

- Modern browsers (Chrome, Firefox, Safari, Edge)
- Responsive design tested at all breakpoints
- CSS Grid and Flexbox support required
- CSS Variables (custom properties) support required

## Testing & Validation

✅ All pages share the same stylesheet
✅ Responsive from 360px to 1200px+ widths
✅ All color variables properly defined
✅ Grid utilities functional
✅ Button states working
✅ Navigation responsive
✅ Tables display correctly
✅ Forms styled consistently
✅ No visual regressions

## Future Customization

To update colors globally, modify the `:root` variables:
- Change `--primary-red` to update all red accents
- Change `--graphite-*` variables to update text/backgrounds
- Update spacing variables for different scale
- Adjust shadow definitions for different depth

All changes will apply site-wide automatically.
