#!/usr/bin/env python3
"""
Restructure with modern Anthropic-inspired design and organized folder structure
"""

from bs4 import BeautifulSoup
import re
import os
import shutil
from pathlib import Path

# Create pages directory
pages_dir = Path('pages')
pages_dir.mkdir(exist_ok=True)

# Read the original HTML file
with open('Complete_30Day_Training_Full.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Modern Anthropic-inspired head section with updated styling
modern_head_template = '''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>{title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <link href="https://fonts.cdnfonts.com/css/opendyslexic" rel="stylesheet">

  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    
    :root {
      /* Light theme (default - Claude style) */
      --bg-primary: #F5F3EF;
      --bg-secondary: #FFFFFF;
      --bg-sidebar: #FDFCFA;
      --text-primary: #1A1A1A;
      --text-secondary: #6B6B6B;
      --text-tertiary: #9B9B9B;
      --accent-orange: #D97757;
      --accent-brown: #8B6B47;
      --border-subtle: #E5E2DC;
      --border-light: #F0EDE7;
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
      --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.07);
      --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.1);
      --radius-sm: 6px;
      --radius-md: 10px;
      --radius-lg: 16px;
    }

    [data-theme="dark"] {
      /* Dark theme (Claude desktop style) */
      --bg-primary: #1F1F1F;
      --bg-secondary: #2B2B2B;
      --bg-sidebar: #242424;
      --text-primary: #ECECEC;
      --text-secondary: #A8A8A8;
      --text-tertiary: #7A7A7A;
      --accent-orange: #E89A7A;
      --accent-brown: #B8936A;
      --border-subtle: #3A3A3A;
      --border-light: #333333;
      --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.3);
      --shadow-md: 0 4px 6px rgba(0, 0, 0, 0.4);
      --shadow-lg: 0 10px 15px rgba(0, 0, 0, 0.5);
    }

    /* Font families */
    html {
      font-family: Candara, 'Gill Sans', 'Gill Sans MT', Calibri, sans-serif;
    }

    [data-font="candara"] {
      font-family: Candara, 'Gill Sans', 'Gill Sans MT', Calibri, sans-serif;
    }

    [data-font="arial"] {
      font-family: Arial, Helvetica, sans-serif;
    }

    [data-font="courier"] {
      font-family: 'Courier New', Courier, monospace;
    }

    [data-font="georgia"] {
      font-family: Georgia, 'Times New Roman', serif;
    }

    [data-font="dyslexic"] {
      font-family: 'OpenDyslexic', sans-serif;
    }

    /* Font sizes */
    html {
      font-size: 16px;
    }

    [data-font-size="small"] {
      font-size: 14px;
    }

    [data-font-size="medium"] {
      font-size: 16px;
    }

    [data-font-size="large"] {
      font-size: 18px;
    }

    [data-font-size="x-large"] {
      font-size: 20px;
    }

    html, body {
      height: 100%;
      background: var(--bg-primary);
      color: var(--text-primary);
      line-height: 1.6;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }

    /* Header */
    #title-block-header {
      background: linear-gradient(135deg, var(--bg-secondary) 0%, var(--bg-primary) 100%);
      border-bottom: 3px solid var(--accent-orange);
      position: sticky;
      top: 0;
      z-index: 1000;
      backdrop-filter: blur(10px);
      box-shadow: var(--shadow-lg);
    }

    .header-row {
      max-width: 1600px;
      margin: 0 auto;
      padding: 1.25rem 2rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 2rem;
    }

    .title {
      font-size: 1.5rem;
      font-weight: 700;
      background: linear-gradient(135deg, var(--accent-orange) 0%, var(--accent-brown) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      letter-spacing: -0.02em;
      margin: 0;
      white-space: nowrap;
    }

    .header-author {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-left: auto;
    }

    .author-name {
      font-size: 0.9rem;
      font-weight: 500;
      color: var(--text-secondary);
      font-style: italic;
    }

    .repo-link {
      display: flex;
      align-items: center;
      color: var(--text-secondary);
      transition: all 0.2s ease;
      padding: 0.25rem;
      border-radius: var(--radius-sm);
    }

    .repo-link:hover {
      color: var(--accent-orange);
      background: var(--bg-primary);
      transform: scale(1.1);
    }

    .repo-link svg {
      display: block;
    }

    .header-controls {
      display: flex;
      gap: 0.5rem;
      align-items: center;
    }

    .font-selector {
      background: var(--bg-primary);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      padding: 0.5rem 0.75rem;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 0.875rem;
      font-weight: 500;
      transition: all 0.2s ease;
      outline: none;
    }

    .font-selector:hover {
      background: var(--bg-secondary);
      border-color: var(--accent-brown);
      color: var(--text-primary);
    }

    .font-selector:focus {
      border-color: var(--accent-orange);
      box-shadow: 0 0 0 3px rgba(217, 119, 87, 0.1);
    }

    .font-size-controls {
      display: flex;
      gap: 0.25rem;
      align-items: center;
    }

    .font-size-btn {
      background: var(--bg-primary);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      width: 2.25rem;
      height: 2.25rem;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 0.75rem;
      font-weight: 600;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .font-size-btn:hover {
      background: var(--bg-secondary);
      border-color: var(--accent-brown);
      color: var(--text-primary);
      transform: translateY(-1px);
    }

    .font-size-btn:active {
      transform: translateY(0);
    }

    .font-size-btn:disabled {
      opacity: 0.4;
      cursor: not-allowed;
    }

    .font-size-btn:disabled:hover {
      background: var(--bg-primary);
      border-color: var(--border-subtle);
      transform: none;
    }

    .theme-toggle {
      background: var(--bg-primary);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      padding: 0.5rem 0.875rem;
      border-radius: var(--radius-sm);
      cursor: pointer;
      font-size: 0.875rem;
      font-weight: 500;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .theme-toggle:hover {
      background: var(--bg-secondary);
      border-color: var(--accent-brown);
      color: var(--text-primary);
    }

    .button {
      background: var(--bg-primary);
      color: var(--text-secondary);
      border: 1px solid var(--border-subtle);
      padding: 0.5rem 0.875rem;
      border-radius: var(--radius-sm);
      font-size: 0.875rem;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .button:hover {
      background: var(--bg-secondary);
      border-color: var(--accent-brown);
      color: var(--text-primary);
      transform: translateY(-1px);
      box-shadow: var(--shadow-sm);
    }

    /* Layout */
    .page {
      max-width: 1600px;
      margin: 0 auto;
      display: flex;
      gap: 2rem;
      padding: 2rem;
      min-height: calc(100vh - 80px);
    }

    /* Modern Sidebar */
    nav#TOC {
      width: 320px;
      min-width: 320px;
      background: var(--bg-sidebar);
      border: 1px solid var(--border-light);
      border-radius: var(--radius-lg);
      padding: 1.5rem;
      align-self: flex-start;
      position: sticky;
      top: 100px;
      max-height: calc(100vh - 120px);
      overflow-y: auto;
      box-shadow: var(--shadow-sm);
      scroll-behavior: smooth;
    }

    nav#TOC::-webkit-scrollbar {
      width: 6px;
    }

    nav#TOC::-webkit-scrollbar-track {
      background: transparent;
    }

    nav#TOC::-webkit-scrollbar-thumb {
      background: var(--border-subtle);
      border-radius: 3px;
    }

    nav#TOC::-webkit-scrollbar-thumb:hover {
      background: var(--accent-brown);
    }

    nav#TOC ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }

    nav#TOC > ul > li {
      margin-bottom: 1.5rem;
    }

    nav#TOC li {
      margin: 0;
    }

    nav#TOC a {
      display: block;
      color: var(--text-secondary);
      text-decoration: none;
      padding: 0.5rem 0.75rem;
      border-radius: var(--radius-sm);
      font-size: 0.8125rem;
      font-weight: 500;
      transition: all 0.2s ease;
      line-height: 1.4;
    }

    nav#TOC > ul > li > a {
      font-weight: 600;
      color: var(--text-primary);
      font-size: 0.875rem;
      margin-bottom: 0.5rem;
    }

    nav#TOC a:hover {
      background: var(--bg-secondary);
      color: var(--accent-orange);
      transform: translateX(2px);
    }

    /* Active page highlighting */
    nav#TOC a.active {
      background: var(--accent-orange);
      color: white;
      font-weight: 600;
    }

    nav#TOC a.active:hover {
      background: var(--accent-brown);
      color: white;
    }

    nav#TOC ul ul {
      margin-top: 0.25rem;
      margin-left: 0.75rem;
      padding-left: 0.75rem;
      border-left: 2px solid var(--border-light);
    }

    /* Content Area */
    .content {
      flex: 1;
      min-width: 0;
      background: var(--bg-secondary);
      border-radius: var(--radius-lg);
      padding: 3rem;
      box-shadow: var(--shadow-sm);
    }

    /* Typography */
    h1 {
      font-size: 2.25rem;
      font-weight: 700;
      color: var(--text-primary);
      letter-spacing: -0.02em;
      margin-bottom: 1.5rem;
      padding-bottom: 1rem;
      border-bottom: 2px solid var(--border-subtle);
    }

    h2 {
      font-size: 1.875rem;
      font-weight: 700;
      color: var(--text-primary);
      letter-spacing: -0.015em;
      margin: 2.5rem 0 1.5rem 0;
      padding: 1.25rem 1.5rem;
      background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%);
      border-left: 4px solid var(--accent-orange);
      border-radius: var(--radius-sm);
      box-shadow: var(--shadow-sm);
    }

    h3 {
      font-size: 1.3rem;
      font-weight: 600;
      color: var(--text-primary);
      margin: 2rem 0 1rem 0;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-light);
    }

    p {
      color: var(--text-secondary);
      margin-bottom: 1rem;
      line-height: 1.7;
    }

    strong {
      color: var(--text-primary);
      font-weight: 600;
    }

    a {
      color: var(--accent-orange);
      text-decoration: none;
      transition: color 0.2s ease;
    }

    a:hover {
      color: var(--accent-brown);
      text-decoration: underline;
    }

    /* External Links with Icon */
    .external-link {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.25rem 0.5rem;
      background: var(--bg-primary);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      font-size: 0.875rem;
      font-weight: 500;
      color: var(--accent-orange);
      transition: all 0.2s ease;
      word-break: break-all;
    }

    .external-link:hover {
      background: var(--accent-orange);
      color: white;
      border-color: var(--accent-orange);
      text-decoration: none;
      transform: translateY(-1px);
      box-shadow: var(--shadow-sm);
    }

    .link-icon {
      flex-shrink: 0;
      opacity: 0.7;
      transition: opacity 0.2s ease;
    }

    .external-link:hover .link-icon {
      opacity: 1;
    }

    /* Lists */
    ul, ol {
      margin: 1rem 0;
      padding-left: 1.5rem;
      color: var(--text-secondary);
    }

    li {
      margin: 0.5rem 0;
      line-height: 1.6;
    }

    /* Code */
    code {
      background: var(--bg-primary);
      color: var(--accent-brown);
      padding: 0.125rem 0.375rem;
      border-radius: 4px;
      font-family: 'SF Mono', 'Monaco', 'Inconsolata', monospace;
      font-size: 0.875em;
      font-weight: 500;
    }

    pre {
      background: var(--bg-primary);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      overflow-x: auto;
      margin: 1.5rem 0;
      position: relative;
    }

    pre code {
      background: none;
      padding: 0;
      color: var(--text-primary);
      font-size: 0.9rem;
      line-height: 1.6;
    }

    /* Copy button for code blocks */
    .copy-btn {
      position: absolute;
      top: 0.75rem;
      right: 0.75rem;
      background: var(--bg-secondary);
      border: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      padding: 0.5rem;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 500;
      cursor: pointer;
      opacity: 0;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      width: 36px;
      height: 36px;
    }

    pre:hover .copy-btn {
      opacity: 1;
    }

    .copy-btn:hover {
      background: var(--accent-orange);
      color: white;
      border-color: var(--accent-orange);
      transform: translateY(-1px);
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }

    .copy-btn.copied {
      background: var(--accent-brown);
      color: white;
    }

    .copy-btn svg {
      flex-shrink: 0;
    }

    /* AI Assistant Buttons - Dynamically Added */
    .ai-assistant-buttons {
      position: absolute;
      bottom: 0.75rem;
      right: 0.75rem;
      display: flex;
      gap: 0.5rem;
      align-items: center;
      opacity: 0;
      transition: opacity 0.2s ease;
    }

    pre:hover .ai-assistant-buttons {
      opacity: 1;
    }

    .ai-quick-btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      padding: 0.5rem 0.75rem;
      border-radius: 6px;
      font-size: 0.8125rem;
      font-weight: 500;
      text-decoration: none;
      transition: all 0.2s ease;
      border: 1px solid;
      min-width: 36px;
      min-height: 36px;
    }

    .chatgpt-btn {
      background: #000000;
      color: white;
      border-color: #333333;
    }

    .chatgpt-btn:hover {
      background: #333333;
      transform: translateY(-1px);
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
      text-decoration: none;
    }

    .claude-btn {
      background: #CC785C;
      color: white;
      border-color: #B86A50;
    }

    .claude-btn:hover {
      background: #B86A50;
      transform: translateY(-1px);
      box-shadow: 0 4px 8px rgba(204, 120, 92, 0.3);
      text-decoration: none;
    }

    .google-btn {
      background: #4285F4;
      color: white;
      border-color: #3B78E7;
    }

    .google-btn:hover {
      background: #3B78E7;
      transform: translateY(-1px);
      box-shadow: 0 4px 8px rgba(66, 133, 244, 0.3);
      text-decoration: none;
    }

    .ai-quick-btn svg {
      flex-shrink: 0;
    }


    /* Tables */
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 1.5rem 0;
      background: var(--bg-secondary);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      overflow: hidden;
    }

    th, td {
      padding: 0.875rem 1rem;
      text-align: left;
      border-bottom: 1px solid var(--border-light);
    }

    th {
      background: var(--bg-primary);
      color: var(--text-primary);
      font-weight: 600;
      font-size: 0.875rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    td {
      color: var(--text-secondary);
    }

    tr:last-child td {
      border-bottom: none;
    }

    /* Horizontal Rule */
    hr {
      border: none;
      height: 1px;
      background: var(--border-subtle);
      margin: 2.5rem 0;
    }

    /* Feedback Bar */
    .feedback-bar {
      background: var(--bg-secondary);
      border-top: 1px solid var(--border-subtle);
      padding: 1.5rem 2rem;
      text-align: center;
      margin-top: 3rem;
    }

    .feedback-bar p {
      margin: 0;
      color: var(--text-secondary);
      font-size: 0.9rem;
    }

    .feedback-link {
      color: var(--accent-orange);
      font-weight: 500;
      text-decoration: none;
      transition: color 0.2s ease;
    }

    .feedback-link:hover {
      color: var(--accent-brown);
      text-decoration: underline;
    }

    /* Practice Notes */
    .practice-note {
      background: var(--bg-primary);
      border: 1px solid var(--border-subtle);
      border-left: 4px solid var(--accent-brown);
      border-radius: var(--radius-sm);
      padding: 1.25rem 1.5rem;
      margin: 1rem 0 1.5rem 0;
    }

    .practice-note p {
      margin-bottom: 0.75rem;
      color: var(--text-primary);
    }

    .practice-note ul {
      margin: 0;
      padding-left: 1.5rem;
    }

    .practice-note li {
      color: var(--text-secondary);
      margin-bottom: 0.5rem;
      line-height: 1.6;
    }

    .practice-note strong {
      color: var(--text-primary);
    }

    /* Back to top - Fixed button */
    .back-to-top {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      width: 3rem;
      height: 3rem;
      background: var(--accent-orange);
      color: white;
      border: none;
      border-radius: 50%;
      font-size: 1.5rem;
      cursor: pointer;
      box-shadow: var(--shadow-lg);
      transition: all 0.3s ease;
      z-index: 999;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: visible;
    }

    .back-to-top::before {
      content: '↑';
      display: block;
    }

    .back-to-top::after {
      content: 'Back to Top';
      position: absolute;
      right: 100%;
      margin-right: 0.75rem;
      background: var(--bg-secondary);
      color: var(--text-primary);
      padding: 0.5rem 1rem;
      border-radius: var(--radius-sm);
      font-size: 0.875rem;
      font-weight: 500;
      white-space: nowrap;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
      box-shadow: var(--shadow-md);
      border: 1px solid var(--border-subtle);
    }

    .back-to-top:hover {
      background: var(--accent-brown);
      transform: translateY(-3px);
      box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
    }

    .back-to-top:hover::after {
      opacity: 1;
    }

    /* Section Cards */
    .section-card {
      background: var(--bg-primary);
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin: 1.5rem 0;
    }

    /* Responsive */
    @media (max-width: 1024px) {
      .page {
        flex-direction: column;
        padding: 1rem;
      }

      nav#TOC {
        position: static;
        width: 100%;
        max-height: none;
        margin-bottom: 2rem;
      }

      .content {
        padding: 2rem 1.5rem;
      }
    }

    @media (max-width: 640px) {
      .header-row {
        padding: 1rem;
      }

      .title {
        font-size: 1rem;
      }

      .content {
        padding: 1.5rem 1rem;
      }

      h1 {
        font-size: 1.75rem;
      }

      h2 {
        font-size: 1.5rem;
      }
    }
  </style>
</head>
'''

# Enhanced scripts with requested features
enhanced_scripts = '''
<script>
document.addEventListener('DOMContentLoaded', function() {
  // 1. Add copy buttons to all code blocks
  document.querySelectorAll('pre').forEach(pre => {
    const button = document.createElement('button');
    button.className = 'copy-btn';
    button.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
      <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
    </svg>`;
    button.setAttribute('aria-label', 'Copy code');
    button.setAttribute('title', 'Copy to clipboard');

    button.addEventListener('click', async () => {
      const code = pre.querySelector('code') || pre;
      const text = code.textContent;

      try {
        await navigator.clipboard.writeText(text);
        button.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>`;
        button.classList.add('copied');
        setTimeout(() => {
          button.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
          </svg>`;
          button.classList.remove('copied');
        }, 2000);
      } catch (err) {
        button.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="18" y1="6" x2="6" y2="18"></line>
          <line x1="6" y1="6" x2="18" y2="18"></line>
        </svg>`;
        setTimeout(() => {
          button.innerHTML = `<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
          </svg>`;
        }, 2000);
      }
    });

    pre.appendChild(button);
  });

  // 1b. Add AI assistant buttons dynamically to AI prompt code blocks
  const aiPromptHeadings = document.querySelectorAll('h3[id*="ai-learning-prompts"]');

  aiPromptHeadings.forEach(heading => {
    // Find ALL code blocks after this heading (until next h2 or h3)
    let currentElement = heading.nextElementSibling;
    const codeBlocks = [];

    while (currentElement) {
      // Stop if we hit another heading
      if (currentElement.tagName === 'H2' || currentElement.tagName === 'H3') {
        break;
      }

      // Collect all PRE elements
      if (currentElement.tagName === 'PRE') {
        codeBlocks.push(currentElement);
      }

      currentElement = currentElement.nextElementSibling;
    }

    // Add buttons to each code block found
    codeBlocks.forEach(codeBlock => {
      // Get the prompt text from THIS specific code block
      const code = codeBlock.querySelector('code') || codeBlock;
      const promptText = code.textContent.trim();

      // Create AI buttons container for THIS prompt
      const aiButtonsContainer = document.createElement('div');
      aiButtonsContainer.className = 'ai-assistant-buttons';

      // ChatGPT button - Black and white icon
      const chatgptBtn = document.createElement('a');
      chatgptBtn.href = 'https://chat.openai.com/?q=' + encodeURIComponent(promptText);
      chatgptBtn.target = '_blank';
      chatgptBtn.className = 'ai-quick-btn chatgpt-btn';
      chatgptBtn.title = 'Open in ChatGPT';
      chatgptBtn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M22.282 9.821a5.985 5.985 0 0 0-.516-4.91 6.046 6.046 0 0 0-6.51-2.9A6.065 6.065 0 0 0 4.981 4.18a5.985 5.985 0 0 0-3.998 2.9 6.046 6.046 0 0 0 .743 7.097 5.98 5.98 0 0 0 .51 4.911 6.051 6.051 0 0 0 6.515 2.9A5.985 5.985 0 0 0 13.26 24a6.056 6.056 0 0 0 5.772-4.206 5.99 5.99 0 0 0 3.997-2.9 6.056 6.056 0 0 0-.747-7.073zM13.26 22.43a4.476 4.476 0 0 1-2.876-1.04l.141-.081 4.779-2.758a.795.795 0 0 0 .392-.681v-6.737l2.02 1.168a.071.071 0 0 1 .038.052v5.583a4.504 4.504 0 0 1-4.494 4.494zM3.6 18.304a4.47 4.47 0 0 1-.535-3.014l.142.085 4.783 2.759a.771.771 0 0 0 .78 0l5.843-3.369v2.332a.08.08 0 0 1-.033.062L9.74 19.95a4.5 4.5 0 0 1-6.14-1.646zM2.34 7.896a4.485 4.485 0 0 1 2.366-1.973V11.6a.766.766 0 0 0 .388.676l5.815 3.355-2.02 1.168a.076.076 0 0 1-.071 0l-4.83-2.786A4.504 4.504 0 0 1 2.34 7.872zm16.597 3.855l-5.833-3.387L15.119 7.2a.076.076 0 0 1 .071 0l4.83 2.791a4.494 4.494 0 0 1-.676 8.105v-5.678a.79.79 0 0 0-.407-.667zm2.01-3.023l-.141-.085-4.774-2.782a.776.776 0 0 0-.785 0L9.409 9.23V6.897a.066.066 0 0 1 .028-.061l4.83-2.787a4.5 4.5 0 0 1 6.68 4.66zm-12.64 4.135l-2.02-1.164a.08.08 0 0 1-.038-.057V6.075a4.5 4.5 0 0 1 7.375-3.453l-.142.08L8.704 5.46a.795.795 0 0 0-.393.681zm1.097-2.365l2.602-1.5 2.607 1.5v2.999l-2.597 1.5-2.607-1.5z"/></svg>';

      // Claude button - Official Anthropic icon
      const claudeBtn = document.createElement('a');
      claudeBtn.href = 'https://claude.ai/new?q=' + encodeURIComponent(promptText);
      claudeBtn.target = '_blank';
      claudeBtn.className = 'ai-quick-btn claude-btn';
      claudeBtn.title = 'Open in Claude';
      claudeBtn.innerHTML = '<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Claude_AI_symbol.svg/1024px-Claude_AI_symbol.svg.png" width="14" height="14" style="display: block;" alt="Claude">';

      // Google button
      const googleBtn = document.createElement('a');
      googleBtn.href = 'https://www.google.com/search?q=' + encodeURIComponent(promptText);
      googleBtn.target = '_blank';
      googleBtn.className = 'ai-quick-btn google-btn';
      googleBtn.title = 'Search in Google';
      googleBtn.innerHTML = '<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z" fill="#4285F4"/><path d="M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z" fill="#34A853"/><path d="M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.07H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.93l2.85-2.22.81-.62z" fill="#FBBC05"/><path d="M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.07l3.66 2.84c.87-2.6 3.3-4.53 6.16-4.53z" fill="#EA4335"/></svg>';

      // Add buttons to container
      aiButtonsContainer.appendChild(chatgptBtn);
      aiButtonsContainer.appendChild(claudeBtn);
      aiButtonsContainer.appendChild(googleBtn);

      // Append to the code block
      codeBlock.appendChild(aiButtonsContainer);
    });
  });

  // 2. Theme toggle functionality (Claude-style)
  const themeToggle = document.getElementById('theme-toggle');
  const themeIcon = document.querySelector('.theme-icon');
  const themeText = document.querySelector('.theme-text');

  // Load saved theme
  const savedTheme = localStorage.getItem('training-theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);
  updateThemeButton(savedTheme);

  function updateThemeButton(theme) {
    if (theme === 'dark') {
      themeIcon.textContent = '☀️';
      themeText.textContent = 'Light';
    } else {
      themeIcon.textContent = '🌙';
      themeText.textContent = 'Dark';
    }
  }

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('training-theme', newTheme);
      updateThemeButton(newTheme);
    });
  }

  // 2b. Font selector functionality
  const fontSelector = document.getElementById('font-selector');

  // Load saved font preference (default to Candara)
  const savedFont = localStorage.getItem('training-font') || 'candara';
  document.documentElement.setAttribute('data-font', savedFont);
  fontSelector.value = savedFont;

  fontSelector.addEventListener('change', (e) => {
    const selectedFont = e.target.value;
    document.documentElement.setAttribute('data-font', selectedFont);
    localStorage.setItem('training-font', selectedFont);
  });

  // 2c. Font size controls
  const fontSizes = ['small', 'medium', 'large', 'x-large'];
  const decreaseBtn = document.getElementById('decrease-font');
  const increaseBtn = document.getElementById('increase-font');

  // Load saved font size (default to medium)
  let currentSizeIndex = fontSizes.indexOf(localStorage.getItem('training-font-size') || 'medium');
  if (currentSizeIndex === -1) currentSizeIndex = 1; // Default to medium

  function applyFontSize(index) {
    document.documentElement.setAttribute('data-font-size', fontSizes[index]);
    localStorage.setItem('training-font-size', fontSizes[index]);

    // Disable buttons at limits
    decreaseBtn.disabled = index === 0;
    increaseBtn.disabled = index === fontSizes.length - 1;
  }

  applyFontSize(currentSizeIndex);

  decreaseBtn.addEventListener('click', () => {
    if (currentSizeIndex > 0) {
      currentSizeIndex--;
      applyFontSize(currentSizeIndex);
    }
  });

  increaseBtn.addEventListener('click', () => {
    if (currentSizeIndex < fontSizes.length - 1) {
      currentSizeIndex++;
      applyFontSize(currentSizeIndex);
    }
  });

  // 3. Highlight active page in TOC and scroll to it
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  const tocLinks = document.querySelectorAll('nav#TOC a');

  tocLinks.forEach(link => {
    const linkHref = link.getAttribute('href');
    if (linkHref === currentPage || linkHref === `../${currentPage}`) {
      link.classList.add('active');

      // Auto-scroll TOC to show active item
      setTimeout(() => {
        const nav = document.querySelector('nav#TOC');
        const linkTop = link.offsetTop;
        const navHeight = nav.clientHeight;
        const linkHeight = link.clientHeight;

        // Scroll so the active link is roughly in the middle
        nav.scrollTop = linkTop - (navHeight / 2) + (linkHeight / 2);
      }, 100);
    }
  });

  // 4. Back to top button functionality
  const backToTopBtn = document.getElementById('back-to-top');
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
});
</script>
'''

def create_toc(current_page=''):
    """Build clean TOC"""
    weeks = [
        ("Week 1: Foundations", "week1.html", list(range(1, 6))),
        ("Week 2: Data Analysis", "week2.html", list(range(6, 11))),
        ("Week 3: Intermediate Concepts", "week3.html", list(range(11, 16))),
        ("Week 4: Advanced Concepts", "week4.html", list(range(16, 21))),
        ("Week 5: Analytics & Optimization", "week5.html", list(range(21, 26))),
        ("Week 6: Mastery & Projects", "week6.html", list(range(26, 31)))
    ]

    day_titles = extract_day_titles()

    toc = ['<ul>']
    toc.append('<li><a href="../index.html" if "pages/" in current_page else "index.html">📚 Training Overview</a></li>')

    for week_name, week_file, days in weeks:
        week_link = f'pages/{week_file}' if current_page == 'index' else week_file
        toc.append(f'<li><a href="{week_link}">{week_name}</a>')
        toc.append('<ul>')
        for day_num in days:
            day_title = day_titles.get(day_num, f"Day {day_num}")
            day_link = f'pages/day{day_num}.html' if current_page == 'index' else f'day{day_num}.html'
            # Shorten titles for TOC
            short_title = day_title.replace('DAY ' + str(day_num) + ': ', '')
            if len(short_title) > 40:
                short_title = short_title[:37] + '...'
            toc.append(f'<li><a href="{day_link}">Day {day_num}: {short_title}</a></li>')
        toc.append('</ul>')
        toc.append('</li>')

    toc.append('</ul>')
    return '\n'.join(toc)

def extract_day_titles():
    """Extract day titles from HTML"""
    day_titles = {}
    all_h2 = soup.find_all('h2')
    for h2 in all_h2:
        if h2.get('id', '').startswith('day-'):
            text = h2.get_text()
            match = re.match(r'DAY (\d+):', text)
            if match:
                day_num = int(match.group(1))
                day_titles[day_num] = text
    return day_titles

def create_html_page(title, toc_html, content_html, current_page=''):
    """Create complete HTML page"""
    modern_head = modern_head_template.replace('{title}', title)
    return modern_head + f'''
<body>
<header id="title-block-header">
  <div class="header-row">
    <h1 class="title">{title}</h1>
    <div class="header-author">
      <span class="author-name">Guru Charan Pathalla</span>
      <a href="https://github.com/gcpathalla/sql_and_excel" target="_blank" class="repo-link" title="View on GitHub">
        <svg width="16" height="16" fill="currentColor" viewBox="0 0 16 16">
          <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.012 8.012 0 0 0 16 8c0-4.42-3.58-8-8-8z"/>
        </svg>
      </a>
    </div>
    <div class="header-controls">
      <select class="font-selector" id="font-selector" aria-label="Select font">
        <option value="candara">Candara</option>
        <option value="arial">Arial</option>
        <option value="courier">Courier New</option>
        <option value="georgia">Georgia</option>
        <option value="dyslexic">OpenDyslexic</option>
      </select>
      <div class="font-size-controls">
        <button class="font-size-btn" id="decrease-font" aria-label="Decrease font size" title="Decrease font size">A-</button>
        <button class="font-size-btn" id="increase-font" aria-label="Increase font size" title="Increase font size">A+</button>
      </div>
      <button class="theme-toggle" id="theme-toggle" aria-label="Toggle theme">
        <span class="theme-icon">🌙</span>
        <span class="theme-text">Dark</span>
      </button>
    </div>
  </div>
</header>
<div class="page">
  <nav id="TOC" role="navigation">
{toc_html}
  </nav>
  <div class="content">
{content_html}
  </div>
</div>
<div class="feedback-bar">
  <p>Have feedback or questions? <a href="mailto:gcpath@live.com?subject=30-Day Excel & SQL Training Feedback" class="feedback-link">Email us at gcpath@live.com</a></p>
</div>
<button class="back-to-top" id="back-to-top" aria-label="Back to top"></button>
{enhanced_scripts}
</body>
</html>'''

def extract_intro_content():
    """Extract intro for index"""
    content = []
    main_h1 = soup.find('h1', id='day-excel-sql-training-plan')
    if main_h1:
        current = main_h1
        while current:
            current = current.find_next_sibling()
            if current and current.name == 'h1' and 'week' in current.get('id', '').lower():
                break
            if current:
                content.append(str(current))
    return '\n'.join(content)


def create_week_summary(week_num, days):
    """Create detailed week summary with day descriptions"""
    day_titles = extract_day_titles()

    week_info = {
        1: {"intro": "This week establishes the foundation for both Excel and SQL. You'll learn core concepts that everything else builds upon.", "focus": "Basic formulas, functions, filtering, lookups, and SELECT queries"},
        2: {"intro": "Week 2 focuses on data analysis fundamentals. Learn to combine data, summarize information, and create meaningful visualizations.", "focus": "JOINs, GROUP BY, pivot tables, charts, and aggregations"},
        3: {"intro": "Move to intermediate concepts with date handling, window functions, and what-if analysis for more sophisticated data work.", "focus": "Date functions, window functions (ROW_NUMBER, RANK, LAG, LEAD), Power Query"},
        4: {"intro": "Master advanced techniques including recursive queries, data modeling, and professional dashboard creation.", "focus": "CTEs, Power Pivot with DAX, CASE statements, PIVOT/UNPIVOT, advanced charts"},
        5: {"intro": "Apply analytics and optimization techniques to real-world scenarios. Learn performance tuning and integration.", "focus": "Statistical analysis, query optimization, advanced aggregations, Excel-SQL integration"},
        6: {"intro": "Final week focuses on mastery-level skills and creating portfolio-ready projects that showcase your abilities.", "focus": "Macros, advanced analytics (cohort, RFM), executive dashboards, final project"}
    }

    info = week_info.get(week_num, {"intro": "", "focus": ""})

    summary = f'''<div class="section-card">
<h2>Week {week_num} Overview</h2>
<p>{info["intro"]}</p>
<p><strong>Key Focus Areas:</strong> {info["focus"]}</p>
</div>

<h2>This Week\'s Learning Path</h2>
<p>Click any day below to view detailed lessons, practice exercises, and assignments:</p>

<div class="section-card">'''

    for day_num in days:
        title = day_titles.get(day_num, f"Day {day_num}")
        topic = re.sub(r'^DAY \d+:\s*', '', title)
        summary += f'''<div style="margin-bottom: 1.5rem;">
<h3 style="margin-bottom: 0.5rem;"><a href="day{day_num}.html" style="color: var(--accent-orange); text-decoration: none;">📚 Day {day_num}: {topic}</a></h3>
<p style="margin-left: 1.5rem; color: var(--text-secondary); font-size: 0.9rem;">Comprehensive 4-hour lesson with tutorials, practice exercises, and assignments</p>
</div>
'''

    summary += '</div>'
    return summary


def extract_week_content(week_num):
    """Extract week content"""
    week_ids = {
        1: 'week-1-foundations',
        2: 'week-2-data-analysis-fundamentals',
        3: 'week-3-intermediate-concepts',
        4: 'week-4-advanced-concepts',
        5: 'week-5-analytics-optimization',
        6: 'week-6-mastery-projects'
    }

    week_id = week_ids.get(week_num)
    if not week_id:
        # Try alternate IDs
        week_id = f'week-{week_num}'

    week_h1 = soup.find('h1', id=lambda x: x and week_id in x if x else False)
    if not week_h1:
        return f"<h1>Week {week_num}</h1><p>Content coming soon...</p>"

    content = [str(week_h1)]
    current = week_h1
    while current:
        current = current.find_next_sibling()
        if current and current.name == 'h1' and current != week_h1:
            break
        if current and current.name == 'h2':
            day_text = current.get_text()
            day_match = re.match(r'DAY (\d+):', day_text)
            if day_match:
                day_num = day_match.group(1)
                content.append(f'<h2><a href="day{day_num}.html">{day_text}</a></h2>')
                continue
        if current:
            content.append(str(current))

    return '\n'.join(content)

def extract_day_content(day_num):
    """Extract day content"""
    all_h2 = soup.find_all('h2')
    day_h2 = None

    for h2 in all_h2:
        if h2.get('id', '').startswith('day-'):
            text = h2.get_text()
            match = re.match(rf'DAY {day_num}:', text)
            if match:
                day_h2 = h2
                break

    if not day_h2:
        return f"<h1>Day {day_num}</h1><p>Content coming soon...</p>"

    content = [str(day_h2)]
    current = day_h2
    while current:
        current = current.find_next_sibling()
        if current and current.name == 'h2' and current.get('id', '').startswith('day-'):
            break
        if current and current.name == 'h1':
            break
        if current:
            content.append(str(current))

    return '\n'.join(content)

# Generate index.html (at root)
print("Generating index.html...")
intro_content = extract_intro_content()
toc = create_toc('index')
index_html = create_html_page(
    '30-Day Excel & SQL Training Plan',
    toc,
    intro_content,
    'index'
)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Generate week pages (in pages/)
week_titles = [
    "Week 1: Foundations",
    "Week 2: Data Analysis Fundamentals",
    "Week 3: Intermediate Concepts",
    "Week 4: Advanced Concepts",
    "Week 5: Analytics & Optimization",
    "Week 6: Mastery & Projects"
]

for week_num in range(1, 7):
    print(f"Generating pages/week{week_num}.html...")
    week_days = list(range((week_num-1)*5+1, week_num*5+1))
    week_summary = create_week_summary(week_num, week_days)
    # Week pages now only show overview + learning path (no redundant content)
    toc = create_toc(f'week{week_num}')
    week_html = create_html_page(
        week_titles[week_num - 1],
        toc,
        week_summary,
        f'week{week_num}'
    )
    with open(f'pages/week{week_num}.html', 'w', encoding='utf-8') as f:
        f.write(week_html)

# Generate day pages (in pages/)
day_titles_dict = extract_day_titles()
for day_num in range(1, 31):
    print(f"Generating pages/day{day_num}.html...")
    day_content = extract_day_content(day_num)
    toc = create_toc(f'day{day_num}')
    day_title = day_titles_dict.get(day_num, f"Day {day_num}")
    day_html = create_html_page(
        day_title,
        toc,
        day_content,
        f'day{day_num}'
    )
    with open(f'pages/day{day_num}.html', 'w', encoding='utf-8') as f:
        f.write(day_html)

print("\n✅ Done! Generated modern design with:")
print("  - index.html (at root)")
print("  - pages/week1-6.html")
print("  - pages/day1-30.html")
print("  - Anthropic-inspired modern design")
print("  - Clean, organized file structure")
