---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-deploying-amazon-workspaces/amazon-workspaces-migrate.html
---

# Amazon WorkSpaces migrate
<a name="amazon-workspaces-migrate"></a>

 Amazon WorkSpaces migrate feature enables you to bring your user volume data to a new bundle. You can use this feature to:
+  Migrate your WorkSpaces from the Windows 7 Experience to the Windows 10 Desktop Experience.
+  Migrate from a PCoIP WorkSpace to a WorkSpaces Streaming Protocol (WSP) WorkSpace.
+  Migrate WorkSpaces from one public, or custom, bundle to another. For example, you can migrate from GPU-enabled (Graphics and GraphicsPro) bundles to non-GPU-enabled bundles, and vice versa.

 **Migration process**

With WorkSpaces migrate, you can specify the target WorkSpaces bundle. The migration process recreates the WorkSpace using a new root volume from the target bundle image, and the user volume from the latest original user volume snapshot. A new user profile is generated during migrate for better compatibility. The data in your old user profile that cannot be moved to the new profile is stored in a .notMigrated folder.

 During migration, the data on the user volume (drive D) is preserved, but all the data on the root volume ( C:\\ drive) is lost. This means that none of the installed applications, settings, and changes to the registry are preserved. The old user profile folder is renamed with the .NotMigrated suffix, and a new user profile is created.

 The migration process takes up to one hour per WorkSpace. In addition, if the migrate workflow fails to complete the process, the service will automatically roll back the WorkSpace to its original state before migration, minimizing any data loss risk.

 Any tags assigned to the original WorkSpace are carried over during migration. The running mode of the WorkSpace is preserved. The migrated WorkSpace has a new WorkSpace ID, computer name, and IP address. **Migration procedure**

You can migrate WorkSpaces through the Amazon WorkSpaces console, the AWS CLI using the [migrate-workspace](https://docs.aws.amazon.com/cli/latest/reference/workspaces/migrate-workspace.html) command, or the Amazon WorkSpaces API. All migration requests get queued, and the service will automatically throttle the total number of migration requests if there are too many. **Migration limits**
+  You cannot migrate to a public or custom Windows 7 desktop experience bundle.
+  You cannot migrate to BYOL Windows 7 bundles.
+  You can migrate BYOL WorkSpaces *only* to other BYOL bundles.
+  You cannot migrate a WorkSpace created from public or custom bundles to a BYOL bundle.
+  Migrating Linux WorkSpaces is not currently supported.
+  In AWS Regions that support more than one language, you can migrate WorkSpaces between language bundles.
+  The source and target bundles must be different. (However, in regions that support more than one language, you can migrate to the same Windows 10 bundle as long as the languages differ.) If you want to refresh your WorkSpace using the same bundle, [rebuild the WorkSpace](https://docs.aws.amazon.com/workspaces/latest/adminguide/rebuild-workspace.html) instead.
+  You cannot migrate WorkSpaces across Regions.
+  WorkSpaces cannot be migrated when they are in ADMIN\_MAINTENANCE mode.

 **Cost**

During the month in which migration occurs, you are charged prorated amounts for both the new and the original WorkSpaces. For example, if you migrate WorkSpace A to WorkSpace B on May 10, you will be charged for WorkSpace A from May 1 to May 10, and you will be charged for WorkSpace B from May 11 to May 30.

 **WorkSpaces migration best practices**

 Before you migrate a WorkSpace, do the following:
+  Back up any important data on drive C to another location. All data on drive C is erased during migration.
+  Make sure that the WorkSpace being migrated is at least 12 hours old, to ensure that a snapshot of the user volume has been created. On the **Migrate WorkSpaces** page in the Amazon WorkSpaces console, you can refer to the time of the last snapshot. Any data created after the last snapshot is lost during migration.
+  To avoid potential data loss, make sure that your users log out of their WorkSpaces, and don't log back in until after the migration process is finished.
+  Make sure that the WorkSpaces you want to migrate have a status of AVAILABLE, STOPPED, or ERROR.
+  Make sure that you have enough IP addresses for the WorkSpaces you are migrating. During migration, new IP addresses will be allocated for the WorkSpaces.
+  If you are using scripts to migrate WorkSpaces, migrate them in batches of no more than 25 WorkSpaces at a time.
