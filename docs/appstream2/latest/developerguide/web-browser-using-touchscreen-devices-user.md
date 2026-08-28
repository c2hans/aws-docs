---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/web-browser-using-touchscreen-devices-user.html
---

# Touchscreen Devices
<a name="web-browser-using-touchscreen-devices-user"></a>

WorkSpaces Applications supports gestures on touch-enabled iPads, Android tablets, and Windows devices. Examples of supported touch gestures include long-tap to right-click, swipe to scroll, pinch to zoom, and two-finger rotation for supporting applications.

**Note**
Touchscreen devices with a screen size of less than 8 inches are not supported.

To display the on-screen keyboard on an iPad or Android tablet, tap the keyboard icon on the WorkSpaces Applications toolbar. The keyboard icon turns blue, and you can use the on-screen keyboard to input text in the streaming application. Tap the keyboard icon again to hide the on-screen keyboard.

![Toolbar with icons for Catalog, Windows, My Files, Clipboard, Microphone, Camera, Preferences, Full screen, Dual monitor, FN Keys, and Profile.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/toolbar-fn-keys.png)

Tap the Fn icon to display a row of Windows-specific keys and keyboard shortcuts.

![Row of icons including grid, folder, and settings symbols, with Fn dropdown highlighted.](http://docs.aws.amazon.com/appstream2/latest/developerguide/images/CircleFnIconBorder.PNG)

For touch-enabled devices, the *remote keyboard*, which is displayed when you tap the keyboard icon on the WorkSpaces Applications toolbar, is different than the *local keyboard*, the on-screen keyboard that a touch-enabled device automatically displays when you tap inside an input control in a locally running application. During WorkSpaces Applications streaming sessions, you can use the remote keyboard to input text into streaming applications only. You can display or hide the remote keyboard only by tapping the keyboard icon on the WorkSpaces Applications toolbar. A blue keyboard icon on the WorkSpaces Applications toolbar indicates that the remote keyboard is active.

You can use the local keyboard to input text into elements of the WorkSpaces Applications web portal, including the **My Files** dialog box. However, you can't use this keyboard to input text into streaming applications. Also, you can't display or hide it by using the keyboard icon on the WorkSpaces Applications toolbar.

**Note**
To display the on-screen keyboard on a Windows computer, tap the keyboard icon in the Windows system tray. If the keyboard icon doesn't appear in the Windows system tray, switch to Windows tablet mode. Tap the keyboard icon in the Windows system tray again to hide the on-screen keyboard.

For more information about function keys, see the next section.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
