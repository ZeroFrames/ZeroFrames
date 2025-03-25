::: mermaid
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

:::
