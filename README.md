<p align="center">
  <img src="docs/logos/1024x1024.png" height="200">
</p>
<h1 align="center">
  ZeroFrames
</h1>

---

> ⭐️ Thanks **everyone** who has starred the project, it means a lot!

🖼️ [ZeroFrames](https://opencollective.com/zeroframes): create your own designs (assets) for the Flipper Zero device.

[![Build Status](https://github.com/ZeroFrames/ZeroFrames/actions/workflows/django.yml/badge.svg)](https://github.com/ZeroFrames/ZeroFrames/actions)
[![License: LGPL v3](https://img.shields.io/badge/License-LGPL%20v3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0)
[![GitHub issues](https://img.shields.io/github/issues/ZeroFrames/ZeroFrames)](https://github.com/ZeroFrames/ZeroFrames/issues)
[![PRs Closed](https://img.shields.io/github/issues-pr-closed/ZeroFrames/ZeroFrames)](https://github.com/ZeroFrames/ZeroFrames/pulls)
[![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)
[![First Timers Friendly](https://img.shields.io/badge/first--timers--only-friendly-blue.svg)](http://www.firsttimersonly.com/)


## Table of content
<details>
<summary>Expand contents</summary>

- [Overview](#overview)
- [News](#news)
- [Installation for Developers](#installation-for-developers)
- [Features](#features)
- [Contributing](#contributing)

</details>

## Overview

ZeroFrames is an easy-to-use tool for creating custom graphics for your Flipper Zero. You can design icons, frames, and other visuals to personalize your device. The tool lets you preview your designs in real-time, export them easily, and even share them with others.

## News

- 🖼️ Created ZeroFrames icon


## Installation for Developers

1. Clone repository:

```bash
git clone https://github.com/ZeroFrames/ZeroFrames.git
```

2. Create and activate virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the ZEROFRAMES

```bash
cd core
```

```bash
python3 manage.py runserver
```

## User Flow

```mermaid
---
config:
  layout: fixed
---
graph TD
    Start[User Visits ZeroFrames] --> Grid[Interactive Pixel Grid Editor]
    subgraph EditorInterface["Editor Interface"]
        Grid --> Tools[Select Drawing Tool]
        Tools -->|Pencil| Draw[Toggle Pixels On/Off]
        Tools -->|Eraser| Erase[Remove Pixels]
        Tools -->|Fill| Fill[Fill Connected Area]
        Tools -->|Line| Line[Draw Straight Line]
        Tools -->|Rectangle| Rect[Draw Rectangle]
        Draw --> EditGrid[Continue Editing Grid]
        Erase --> EditGrid
        Fill --> EditGrid
        Line --> EditGrid
        Rect --> EditGrid
        EditGrid --> Preview[Preview Current Frame]
    end
    subgraph AnimationTimeline["Animation Features"]
        Preview --> ManageFrames[Manage Animation Frames]
        ManageFrames -->|Add Frame| NewFrame[Create New Frame]
        ManageFrames -->|Delete Frame| DeleteFrame[Remove Frame]
        ManageFrames -->|Duplicate| DuplicateFrame[Duplicate Frame]
        ManageFrames -->|Reorder| ReorderFrames[Reorder Frames]
        NewFrame --> EditGrid
        DeleteFrame --> EditGrid
        DuplicateFrame --> EditGrid
        ReorderFrames --> EditGrid
        ManageFrames --> PlayAnimation[Play Animation Preview]
        PlayAnimation --> AdjustSpeed[Adjust Animation Speed]
        AdjustSpeed --> PlayAnimation
    end
    subgraph FileOperations["File Operations"]
        EditGrid --> SaveProject[Save Project]
        PlayAnimation --> SaveProject
        SaveProject --> Export[Export Options]
        Export -->|.txt Format| ExportTXT[Export as .txt]
        Export -->|.fbz Format| ExportFBZ[Export as .fbz]
        ExportTXT --> Download[Download File]
        ExportFBZ --> Download
        Grid --> Import[Import Existing File]
        Import -->|.txt Format| ImportTXT[Import .txt File]
        Import -->|.fbz Format| ImportFBZ[Import .fbz File]
        ImportTXT --> Grid
        ImportFBZ --> Grid
    end
    subgraph SharingOptions["Sharing Options"]
        Download --> Share[Share Creation]
        Share -->|Generate Link| ShareLink[Create Shareable Link]
        Share -->|Social Media| ShareSocial[Share to Social Media]
        ShareLink --> CopyLink[Copy Link to Clipboard]
        ShareSocial --> PostToSocial[Post to Selected Platform]
    end
    EditGrid -.-> SaveProject
    PlayAnimation -.-> SaveProject
```

---


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

<a href="https://github.com/DeepBlackHole/ZeroFrames/graphs/contributors">
  <img
    src="https://opencollective.com/ZeroFrames/contributors.svg?width=890&button=false"
    alt="Contributors"
  />
</a>
