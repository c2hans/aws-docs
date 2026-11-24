---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/edit-assets-in-the-portal.html
---

# Edit assets in the Portal

You change an asset in the Spatial Data Portal as a working copy. Every change you make, such as adding, moving, renaming, or removing files, is staged. You review the staged changes and save them together as one new asset version.

You need permission to update the asset. For details, see [Access Management](access-control.md).

**Note**
You must use Spatial Data Portal desktop application version 0.2.8 or later to place, rename, move, and drop files, to use **Sync from local folder**, and to see transfer progress in the menu bar or tray. If your desktop application is older, the Portal hides those controls. Install the latest desktop application from [Client setup](client-setup.md).

## The Working Copy
<a name="edit-working-copy"></a>

Staged changes appear in the file tree. Badges mark each one as **Added**, **Edited**, or **Removed**, and a folder shows the total for the files under it. A row has an undo button when it has a staged change.

You can stage these changes:
+ Add files and folders.
+ Replace a file.
+ Move or rename a file or folder.
+ Remove files and folders.
+ Create a folder.
+ Edit a file’s attributes, or the asset’s details and attributes.

When changes are staged:
+ Automatic refresh of the file list pauses.
+ The Portal checks the working copy against the asset’s template as you work. You can save only when it conforms.
+ Some actions, such as **Compare files** and **Download**, wait until you save or discard.

## Review and Save
<a name="edit-review-save"></a>

1. Choose **Review and save**. The list shows every change: added, moved, renamed, edited attributes, removed, and asset details.

1. Choose **Save**. The Portal saves all the changes as a single new version of the asset.

To drop all staged changes, choose **Discard**.

When a save runs, **Review and save** and **Discard** are locked, and staged rows read **Adding**, **Editing**, and so on. The staged changes stay on screen until the new version’s file list has loaded. If the save fails, pauses, or is canceled, your changes are kept so that you can try again.

## Edit Attributes of Many Files at Once
<a name="edit-file-attributes"></a>

Templates often require the same attributes on every file, such as a sensor, a capture date, or a coordinate system. You can set them for many files in one step, instead of opening each file.

1. On the asset’s **Files** tab, choose **Edit attributes** from the file actions. What it acts on depends on what is selected:
   + With files selected, **Edit attributes** acts on those files.
   + With one folder selected, it acts on the files in that folder.
   + With nothing selected, it acts on the files on show: **Edit attributes of all files** for the whole asset, **Edit attributes of all files here** for the folder that is open, or **Edit attributes of matching files** when a file filter is active.

1. In the **Edit attributes** window, choose how to work:
   +  **By type** – Edit the attributes that files of a type share. Each section shows the files it covers, so a change to **LAZ** files applies to every LAZ file in the scope. Use **Apply to** to narrow the files.
   +  **By file** – Pick a file from the list and edit its attributes alone. The attributes of the file you picked are beside the list.

1. Choose **Done**. The edits are staged in the working copy, with an **Edited** badge on each affected row. They are saved with your other changes when you choose **Review and save**.

An attribute that the template requires shows as missing until you set it. The window warns when some files are missing required attributes. System files and derived files cannot have attributes, and are left out of the scope.

Attributes that a connector run wrote keep the run as their source. When you change a value, SDMA records the new value as yours. A value that you leave unchanged keeps its source.

## Add, Move, and Rename Files
<a name="edit-add-move"></a>
+  **Add.** Choose **Add files**, or use the menu next to it to **Add folder**. You can also drag files and folders from your computer into the file tree. A dropped folder keeps its name and everything in it.
+  **Where files go.** With nothing selected, adding files, creating a folder, and dropping files act on the folder that is on show. Dropping on a folder puts the files in that folder.
+  **Move.** Drag rows to a folder. If several rows are selected, dragging one moves all of them. Or choose **Move to** to browse the asset one level at a time, find a folder by path, or create one. A moved folder’s full contents are loaded first, so nothing is left behind.
+  **Rename.** Choose **Rename** on a row.
+  **Replace.** Choose **Replace** on a file to replace it in place.
+  **Reuse of content.** A move or rename reuses the existing content, so nothing is uploaded again.

Files that SDMA keeps for the asset, under `.spatial_data_mgmt`, cannot be renamed, moved, replaced, removed, or edited. Derived output, under `.spatial_data_mgmt_derived`, can be removed, because a connector can make it again. It cannot be changed in any other way.

## Moved and Renamed Files Keep Their History
<a name="edit-moves-keep-history"></a>

When you save a version in which a file was moved or renamed, SDMA recognizes it as the same file.
+ The version history lists the file as **moved**, with its previous path.
+ The file keeps its attributes, attribute suggestions, analysis results, connected resources, and connector results. It is not analyzed again, and connectors do not run for it again.
+ Connector runs from before the move still show in the file’s runs.

SDMA records a move only when the manifests prove it: the old path is gone, the new path is new, and the content is identical. If a file changed as well as moved, it appears as a removed file and an added file.

## Sync from Local Folder
<a name="edit-sync"></a>

 **Sync from local folder** makes an asset match a folder on your computer.

1. Choose **Sync from local folder** and choose the folder.

1. The Portal compares the folder with the asset by content. A single table lists every added, edited, and removed file, with the same badges as the file tree. The table is paged and can be filtered.

1. To leave a change out, choose its undo arrow. If you skip a removal, the file stays in the asset.

1. Confirm to apply the changes. Exactly the changes you previewed run, and removals ask for confirmation first.

The asset’s own files, such as system bookkeeping and derived content, are never removed.

## Create an Asset from Files and Folders
<a name="edit-create-asset"></a>

In the create asset wizard, the content step works the same way. Pick or drop files and folders, review them in the paged table, and create the asset. The step checks the content against the template as you change it.

The wizard then offers an optional **Set file attributes** step. It is the same editor as **Edit attributes**, so you can give the files you are adding their attributes before the asset exists. The step title shows how many required values are still missing, for example **Set file attributes (12 required missing)**. The review step shows the content, the asset attributes, and the file attributes as tabs. Files that you add by Amazon S3 import get their attributes after the asset is created.

## Browser Limits
<a name="edit-browser-limits"></a>

Saves from the browser are held to the browser upload limits in [Client setup](client-setup.md). If your staged changes are over a limit, an alert shows which limit and offers **Open desktop app**, and **Save** is disabled until the set fits. The desktop application has no such limits.

## Transfers
<a name="edit-transfers"></a>

Uploads, downloads, saves, and deletes appear in the **Transfers** menu next to **Notifications**.
+ Each transfer shows progress. You can pause, resume, cancel, and retry. Pause is not offered when files are being checked or for downloads.
+ A short message beside the button says when transfers start and finish. A failure stays until you dismiss it, and shows the full error.
+ Deleting one or many assets reports there. A failed delete does not stop the others, and the failed assets stay selected.
+ Leaving the page during a browser upload asks you first. Signing out or switching profile when transfers run asks first too.
+ In the desktop application, transfers also show in the menu bar or tray.

## Download Files
<a name="edit-downloads"></a>
+ In the desktop application, **Download** opens the download dialog.
+ In a browser, the same button reads **Download copy**. **Download asset** explains that downloading a whole asset needs the desktop application.
+ Downloads from a file’s history fetch the version you chose, not the latest.

## Open a Page in the Desktop Application
<a name="edit-open-desktop"></a>

In a browser, you can send a page or a download to the desktop application. The desktop application opens its download dialog and shows that the request came from a link. Nothing transfers until you confirm. You can turn this option off in App settings.

## App Settings
<a name="app-settings"></a>

 **App settings** holds your personal Portal preferences:
+ Map style.
+ Whether hidden files show, and where derived files appear in an asset’s file list.
+ 3D viewer defaults: auto-rotate, up axis, background, guides, edge darkening, and splat detail.
+ Download location.
+ Desktop application shortcuts.
+ Whether the sidebar is expanded.
+ Recent searches, and a reset for table preferences.
+ The solution version and third-party licenses.
