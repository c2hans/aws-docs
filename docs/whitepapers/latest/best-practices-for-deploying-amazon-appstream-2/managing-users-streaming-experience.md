---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/managing-users-streaming-experience.html
---

# Managing users’ streaming experience
<a name="managing-users-streaming-experience"></a>

## Customization using session scripts
<a name="customization-using-session-scripts"></a>

 WorkSpaces Applications provides on-instance session scripts. You can use these scripts to run your own custom scripts when specific events occur in users' streaming sessions. For example, you can use custom scripts to prepare your WorkSpaces Applications environment before your users' streaming sessions begin. You can also use custom scripts to clean up streaming instances after users complete their streaming sessions.

 Specify session scripts within a WorkSpaces Applications image. For more information on configuring session scripts, review the administration guide’s section on [using session scripts to manage your user’s experience](https://docs.aws.amazon.com/appstream2/latest/developerguide/use-session-scripts.html). Used with a network share or [https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) (IAM) profile, you can use session scripts to retrieve additional scripting from a storage location. With this additional scripting, you can run further user experience optimization. This can minimize the number of images and fleets required to deliver application environments to your users.

## Using Active Directory Group Policy
<a name="using-active-directory-group-policy"></a>

 If you are planning to use WorkSpaces Applications fleets in an Active Directory domain, you can use Group Policies Objects (GPOs) to manage user experience. GPOs can be assigned to the Organizational Unit (OU) in which the WorkSpaces Applications instances are created. To simplify image creation, launch the base WorkSpaces Applications Image in an OU that blocks inheritance. This prevents other domain policies impacting the WorkSpaces Applications user experiences. Deploy each fleet into its dedicated OU, with unique GPOs establishing the environment allows the one-to-many consolidated benefit of WorkSpaces Applications image management.

 An example of using Group Policy is to specify image set [https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets.html#customize-fleets-change-ie-homepage-group-policy](https://docs.aws.amazon.com/appstream2/latest/developerguide/customize-fleets.html#customize-fleets-change-ie-homepage-group-policy).
