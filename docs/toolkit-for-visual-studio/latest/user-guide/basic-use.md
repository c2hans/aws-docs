---
source_url: https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/basic-use.html
---

# Profiles and Window Binding
<a name="basic-use"></a>

## Profiles and Window Binding for the Toolkit for Visual Studio
<a name="profiles-and-tvs-window-binding"></a>

When working with the publishing tools, wizards, and other features of the Toolkit for Visual Studio, take note of the following:
+ The AWS Explorer window is bound to a single profile and region at a time. Windows opened from the AWS Explorer default to that bound profile and region.
+ After a new window has been opened, you can use that instance of the AWS Explorer to switch to a different profile or region.
+ The Toolkit for Visual Studio publishing tools and features automatically default to the profile and region set in the AWS Explorer.
+ If a new profile or region is specified in a publishing tool, wizard, or feature: all resources created afterwards will continue to use the new profile and region settings.
+ If you have multiple instances of Visual Studio open, each instance can be bound to a different profile and region.
+ The AWS Explorer saves the last profile and region that were specified and the very last Visual Studio instance closed will have its values persisted.
