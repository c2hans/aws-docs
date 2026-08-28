---
source_url: https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/environment-software-sets.html
---

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ag/workspacesthinclient-end-of-support.html).

# WorkSpaces Thin Client software releases
<a name="environment-software-sets"></a>

WorkSpaces Thin Client is an AWS End User Computing service that provides users access to virtual desktops on a device. These devices are periodically updated with new software sets. The following table describes all the released software sets. Administrators can use the [AWS management console](https://aws.amazon.com) to view available software sets.

| Software set | Release date | Changes |
| --- | --- | --- |
| 2.20.3 | 03-19-2026 |  + Fix for Chromium's CVE-2026-3909 and CVE-2026-3910 critical security issues.  |
| 2.20.2 | 02-23-2026 |  + Fix for Chromium's CVE-2026-2441 critical security issue.  |
| 2.20.1 | 11-18-2025 |  + Fix for Chromium's CVE-2025-13223 and CVE-2025-13224 critical security issues.  |
| 2.20.0 | 11-5-2025 |  + Improves the authentication of the device.  |
| 2.19.0 | 9-30-2025 |  + Toolbar actions such as **Restart**, **Shut down**, and **Sleep** now require end users to re-authenticate with WorkSpaces.<br />+ Fixed an issue where end users were unable to use Ctrl\+Space keys to select the column in Excel.<br />+ Changed the internal URLs for Lock and Licensing pages.  |
| 2.18.0 | 8-28-2025 |  + Added **Exit Session** button to the device toolbar.<br />+ Fixed an issue where activity status notification was incorrectly shown on the device.<br />+ Added support for FIDO2 in session authentication.<br />+ General fixes and improvements.  |
| 2.17.0 | 7-30-2025 |  + [Plugable USB hub UD-3900Z](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/usb-hub-specifications.html) is now supported for use with WorkSpaces Thin Client.<br />+ Added support for AltGr keys with Spanish keyboards.<br />+ Fixed the issue that resulted in duplicate entries for user session activity for the device.<br />+ Added support for Enter key on numeric keypad.<br />+ General fixes and improvements.  |
| 2.16.2 | 7-22-2025 |  + Fix for Chromium's CVE-2025-6558 critical security issue.  |
| 2.16.1 | 7-3-2025 |  + Fix for Chromium's CVE-2025-6554 critical security issue.  |
| 2.16.0 | 6-27-2025 |  + Added notifications for Network Latency.<br />+ Added ability to recover from second monitor going dark during a session.<br />+ Fixed issue with monitors showing a white screen or not auto extending after the device comes back from sleep mode.  |
| 2.15.0 | 6-19-2025 |  + Added support for Latin America Spanish and International English keyboards.<br />+ End users see notifications when device does not detect keyboard or mouse activity for extended amount of time.  |
| 2.14.1 | 6-09-2025 |  + Fix for Chromium's CVE-2025-5419 critical security issues.  |
| 2.13.0 | 3-31-2025 |  + End users will see product satisfaction feedback survey as a notification.<br />+ Adds prerelease feature support for FIDO2 authentication flow. See [FIDO2 pre-session details](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/known-issues.html#fido2-prerelease).<br />+ The device will not go to sleep if audio/video is playing in the session.<br />+ End users see notifications when monitor is connected and disconnected.<br />+ Device collects diagnostic information from the operation system for service improvements.<br />+ Fixes an issue where an incorrect date was shown in Settings for software installed date.  |
| 2.14.0 | 4-29-2025 |  + Usability improvements and bug fixes.  |
| 2.13.0 | 3-31-2025 |  + End users will see product satisfaction feedback survey as a notification.<br />+ Adds prerelease feature support for FIDO2 authentication flow. See [FIDO2 pre-session details](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/known-issues.html#fido2-prerelease).<br />+ The device will not go to sleep if audio/video is playing in the session.<br />+ End users see notifications when monitor is connected and disconnected.<br />+ Device collects diagnostic information from the operation system for service improvements.<br />+ Fixes an issue where an incorrect date was shown in Settings for software installed date.  |
| 2.12.0 | 1-30-2025 |  + Fixes an issue where end user was logged out of session on pressing the back button on mouse.  |
| 2.11.2 | 1-24-2025 |  + Fixes an issue where audio was crackling during calls with mouse movements across monitors.  |
| 2.11.1 | 12-27-2024 |  + Fixes dual monitor auto-extend issue.<br />+ Minor improvements to VoiceView label.  |
| 2.11.0 | 12-19-2024 |  + WorkSpaces Thin Client now supports VoiceView and Magnifier.  |
| 2.10.0 | 11-22-2024 |  + End users can use a keyboard shortcut to collapse the device toolbar.  |
| 2.9.0 | 10-28-2024 |  + Administrators can now view their end users' device settings within AWS console under Device details page of a specific device.<br />+ WorkSpaces Thin Client now supports 2K resolution monitor for single screen.<br />+ End users can see notifications related to network diagnostics on their WorkSpaces Thin Client devices.<br />+ End user can now choose to place device toolbar on left or right as per their preference.<br />+ Fixed an issue where device did not install software updates during sleep or idle time.  |
| 2.8.1 | 09-26-2024 |  + Fixed a critical issue where the second monitor could not be toggled on after the device woke up from sleep.  |
| 2.8.0 | 09-06-2024 |  + Thin Client supports monitors with 4K resolution.<br />+ Users can connect to the VDI session even if WorkSpaces Thin Client device management services are temporarily unavailable.<br />+ Fixed the issue where User activity details section in AWS console showed duplicate entries.<br />+ End users can use PrintScreen option while streaming WorkSpaces on WorkSpaces Thin Client.  |
| 2.7.1 | 08-27-2024 |  + Zero-day fixes for Chromium's CVE-2024-7971 and CVE-2024-7965 critical security issues.  |
| 2.7.0 | 07-29-2024 |  + Improvements to performance of second monitor.<br />+ Fixed an issue where the toolbar language was unaffected on changing device language.<br />+ Device now collects diagnostic information for service improvements.  |
| 2.6.0 | 07-09-2024 |  + Users can defer the incoming software updates so that they can finish their work without interruption.<br />+ Device settings allows users to forget saved WiFi networks.<br />+ Improvements to performance of audio/video calls in the session.<br />+ Some user settings for the VDI sessions persist across device reboot.  |
| 2.5.0 | 06-13-2024 |  + Fixed the issue where device showed keyboard and mouse setup screen briefly on waking up from sleep before launching the session.<br />+ The **Home** button on the device toolbar renamed to **Sign In**.<br />+ Improvements to performance of audio/video calls in the session.  |
| 2.4.3 | 05-29-2024 |  + Zero-day fix for Chromium's CVE-2024-5274 critical security issue.  |
| 2.4.2 | 05-17-2024 |  + Zero-day fix for Chromium's CVE-2024-4947 critical security issue.  |
| 2.4.1 | 05-15-2024 |  + Zero-day fixes for Chromium's CVE-2024-4671 and CVE-2024-4761 critical security issues.<br />+ Fixed the issue that allowed right-clicking on AWS and Privacy links on WorkSpaces sign-in page to open the browser in a stand-alone mode.  |
| 2.4.0 | 05-09-2024 |  + Fixed an issue blocking "accounts.google.com" and preventing the use of Google Workspace as the IDP for WorkSpaces Applications session.<br />+ Device settings toolbar auto-collapses with a click in any area on the screen.  |
| 2.3.0 | 04-05-2024 |  + Device settings show up in a collapsed toolbar allowing better utilization of the visible screen.<br />+ End users can now configure the duration to wait before the device sleeps on inactivity.<br />+ Fixed the issue where "about:blank" URL shows up on the second display.<br />+ Fixed the issue that resulted in a white screen when extended display is closed.<br />+ Volume levels set by end users now persists across device restarts.  |
| 2.2.1 | 02-16-2024 |  + Fixed an issue that occurs during the sign-in process that prevented users from logging into WorkSpaces configured with SAML 2.0 authentication.  |
| 2.2.0 | 02-08-2024 |  + Added support for ISO keyboards with English (United Kingdom), French, German, Italian, Spanish locales.   |
| 2.1.2 | 01-26-2024 |  + Zero-day fix for Chromium's CVE-2024-0519 critical security issue.<br />+ Improvement to end user latency associated with Lock functionality.<br />+ Internal device-facing endpoints are switched over to 'thinclient\*' domain.  |
| 2.1.1 | 12-21-2023 |  + Zero-day fix for Chromium's CVE-2023-7024 critical security issue.  |
| 2.1.0 | 12-20-2023 |  + Adds a **Home** button to the device settings and enables support for Meta keys. This allows ends users to invoke the lock screen by pressing Meta\+L.  |
| 2.0.1 | 12-06-2023 |  + Zero-day fix for Chromium's CVE-2024-6345 critical security issue.  |
| 2.0.0 | 11-15-2023 |  + Initial release  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Thin Client. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query workspaces-thin-client` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
