---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/configure-default-regional-settings.html
---

# Configure Default Regional Settings for Your WorkSpaces Applications Users
<a name="configure-default-regional-settings"></a>

**Note**
The instructions on this page only apply to Windows fleets. Default regional settings are not supported for Elastic fleets.

In WorkSpaces Applications, users in a Windows stack can configure their streaming sessions to use settings that are specific to their location or language. For more information, see [Enable Your WorkSpaces Applications Users to Configure Their Regional Settings](regional-settings.md). You can also configure your fleets to use default settings that are specific to your users’ location or language. In particular, you can apply the following Windows settings to your fleets:
+ **Time Zone** — Determines the system time used by Windows and any applications that rely on the operating system time. WorkSpaces Applications makes available the same options for this setting as Windows Server 2019 or later.
+ **Display Language** — Determines the display language used by the Windows operating system and certain Windows applications.
+ **System Locale** — Determines the code pages (ANSI, MS-DOS, and Macintosh) and bitmap font files that Windows uses for non-Unicode applications in different languages.
+ **User Locale** (also known as culture) — Determines the conventions used by Windows and any applications that query the Windows culture when formatting dates, numbers, or currencies or when sorting strings.
+ **Input Method** — Determines the keystroke combinations that can be used to enter characters in another language.

Currently, WorkSpaces Applications supports English and Japanese only for these language settings.

**Topics**
+ [Specify a Default Time Zone](configure-default-time-zone.md)
+ [Specify a Default Display Language](configure-default-display-language.md)
+ [Specify a Default System Locale](configure-default-system-locale.md)
+ [Specify a Default User Locale](configure-default-user-locale.md)
+ [Specify a Default Input Method](configure-default-input-method.md)
+ [Configuring Chinese and Korean input methods on the image](configure-chinese-korean-input-methods.md)
+ [Special Considerations for Application Settings Persistence](special-considerations-app-settings-persistence.md)
+ [Special Considerations for Japanese Language Settings](special-considerations-japanese-language-settings.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
