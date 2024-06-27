# Ninja Markdown Plugin

Welcome! This project aims to enhance your productivity by providing advanced Markdown formatting features. The current version of the application is a Python script that runs from the desktop command line on Windows 10 or 11.

## Project Overview

The **Ninja Markdown Plugin** is designed to streamline the creation and formatting of Markdown documents. This plugin provides a utility to automatically generate a Table of Contents (ToC) from any Markdown file. It updates headers to be clickable links, facilitating quick navigation within the document. This tool is particularly useful for improving productivity and managing large Markdown note files.

## Why Use This Plugin

Markdown is a lightweight markup language with plain-text formatting syntax. Its simplicity and ease of use have made it popular for a variety of applications, including note-taking, documentation, and content creation. Here are some advantages:

- **Readable and Writeable:** Markdown’s syntax is easy to read and write, which makes it great for quick note-taking and documentation.
- **Versatile:** Markdown can be converted to many formats (HTML, PDF, etc.) and is used in a wide range of applications from websites to technical documentation.
- **Compatibility:** Many note-taking apps support Markdown, allowing for seamless integration and greater productivity.

## Installation and Setup

### Prerequisites

- **Python:** Ensure you have Python installed on your system. You can download it from the [official website](https://www.python.org/downloads/).

### Instructions (Windows 10 or 11)

1. **Clone the repository:**
    ```shell
    git clone https://github.com/Zenetusken/NinjaMarkdown.git
    ```
    
2. **Navigate to the project directory:**
    ```shell
    cd NinjaMarkdown
    ```
    
3. **Place the Python script in a convenient directory.**
    
4. **Run the script:** Open your command line interface and execute the script using Python, alternately you can use a relative path of your Markdown file as long as you're inside the script folder when executing this command:
    ```shell
    python headers.py <filename>
    ```

### Example Usage

The script is designed to be used with Markdown flavored formatting, providing various utilities for handling Markdown files.

<p align="center">
  <img src="https://github.com/Zenetusken/NinjaMarkdown/assets/173852206/f12a99c4-971c-452d-a02b-ad90ec7fbff7" alt="Markdown Example 1" style="border: 3px solid white; padding: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);">
</p>

- *To run the script, simply use the command*:
  ```shell
  C:\Users\user\OneDrive\Documents\Obsidian Vault> python headers.py "C:\Bakcup\Obsidian Bakcup\Notes\mynote.md"
  Success!
  ```

- *We get*:

<p align="center">
  <img src="https://github.com/Zenetusken/NinjaMarkdown/assets/173852206/6c60c51c-40d4-4ab6-a7f9-bd1a38802369" alt="Markdown Example 2" style="border: 3px solid white; padding: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);">
</p>

Here are some specific uses of Markdown and the advantages it brings:

- **Notes and Documentation:** Easily create well-structured ToC for .md files on-the-fly.
- **Why Markdown?** It's widely supported by many note-taking apps such as [Obsidian](https://obsidian.md/), [Joplin](https://joplinapp.org/) as well as [Notion](https://www.notion.so/desktop) that are all powerhouses for note-taking and are integrated with a plethora of extra features including AI.
- **Integration with Other Tools:** Markdown serves as a baseline for other tools such as parsers for various programming languages, enabling seamless integration and processing for developers.

## Features

- **Automatic Table of Contents:** Generates a ToC for your Markdown document.
- **Clickable Headers:** Each header becomes a clickable link for quick navigation within the document.
- **Support for multiple headers of the same name:** Links to the correct one inside the document (e.g., "Exercises").
- **In-place Updates:** The script updates the existing Markdown file without creating a new one.

## Future Plans

Currently, these instructions are for a Windows-based environment, specifically Windows 10 or 11. In the future, the plugin will be directly integrated with Obsidian, which I consider the most advanced and robust editor available.

### Upcoming features list:

- [ ] Dynamically autogenerated list
- [ ] More readable and functional
- [ ] Improve the formatting and design
- [ ] More integration and features!

## Getting Help

If you encounter any issues, questions, comments, or have a feature request for the plugin or for more formatting choices to be supported, feel free to email me at [andre.zen799@gmail.com](mailto:andre.zen799@gmail.com).

## Maintainers

- [Andrei P.](https://github.com/Zenetusken)

## License

My own personal work and open source.

_This README file will be continuously updated to include more features and improvements. Stay tuned for updates!_

## Version tracker

- 1.0.0 [*Created branching to support future changes to the repository*]
