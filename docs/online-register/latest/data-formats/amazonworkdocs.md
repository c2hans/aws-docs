---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonworkdocs.html
---

# Data retrieval APIs for Amazon WorkDocs
<a name="amazonworkdocs"></a>

Amazon WorkDocs provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="workdocs-CheckAlias"></a>[https://docs.aws.amazon.com/workdocs/latest/adminguide/cloud_quick_start.html](https://docs.aws.amazon.com/workdocs/latest/adminguide/cloud_quick_start.html) | Check an alias | Read |
| <a name="workdocs-DescribeActivities"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeActivities.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeActivities.html) | Fetch user activities in a specified time period | List |
| <a name="workdocs-DescribeAvailableDirectories"></a>[https://docs.aws.amazon.com/workdocs/latest/adminguide/getting_started.html](https://docs.aws.amazon.com/workdocs/latest/adminguide/getting_started.html) | Describe available directories | List |
| <a name="workdocs-DescribeComments"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeComments.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeComments.html) | List all the comments for the specified document version | List |
| <a name="workdocs-DescribeDocumentVersions"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeDocumentVersions.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeDocumentVersions.html) | Retrieve the document versions for the specified document | List |
| <a name="workdocs-DescribeFolderContents"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeFolderContents.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeFolderContents.html) | Describe the contents of the specified folder, including its documents and sub-folders | List |
| <a name="workdocs-DescribeGroups"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeGroups.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeGroups.html) | Describe the user groups | List |
| <a name="workdocs-DescribeInstanceExports"></a>[https://docs.aws.amazon.com/workdocs/latest/adminguide/migration-tool.html](https://docs.aws.amazon.com/workdocs/latest/adminguide/migration-tool.html) | Describe the export history for an instance | List |
| <a name="workdocs-DescribeInstances"></a>[https://docs.aws.amazon.com/workdocs/latest/adminguide/getting_started.html](https://docs.aws.amazon.com/workdocs/latest/adminguide/getting_started.html) | Describe instances | List |
| <a name="workdocs-DescribeNotificationPermissions"></a>[https://docs.aws.amazon.com/workdocs/latest/adminguide/manage-notifications.html](https://docs.aws.amazon.com/workdocs/latest/adminguide/manage-notifications.html) | Describe principals that are allowed to call notification subscription APIs for a given WorkDocs site | List |
| <a name="workdocs-DescribeNotificationSubscriptions"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeNotificationSubscriptions.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeNotificationSubscriptions.html) | List the specified notification subscriptions | List |
| <a name="workdocs-DescribeResourcePermissions"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeResourcePermissions.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeResourcePermissions.html) | View a description of a specified resource's permissions | List |
| <a name="workdocs-DescribeRootFolders"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeRootFolders.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeRootFolders.html) | Describe the root folders | List |
| <a name="workdocs-DescribeUsers"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeUsers.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_DescribeUsers.html) | View a description of the specified users. You can describe all users or filter the results (for example, by status or organization) | List |
| <a name="workdocs-DownloadDocumentVersion"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetDocumentVersion.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetDocumentVersion.html) | Download a specified document version | Read |
| <a name="workdocs-GetCurrentUser"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetCurrentUser.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetCurrentUser.html) | Retrieve the details of the current user | Read |
| <a name="workdocs-GetDocument"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetDocument.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetDocument.html) | Retrieve the specified document object | Read |
| <a name="workdocs-GetDocumentPath"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetDocumentPath.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetDocumentPath.html) | Retrieve the path information (the hierarchy from the root folder) for the requested document | Read |
| <a name="workdocs-GetDocumentVersion"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetDocumentVersion.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetDocumentVersion.html) | Retrieve version metadata for the specified document | Read |
| <a name="workdocs-GetFolder"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetFolder.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetFolder.html) | Retrieve the metadata of the specified folder | Read |
| <a name="workdocs-GetFolderPath"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetFolderPath.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetFolderPath.html) | Retrieve the path information (the hierarchy from the root folder) for the specified folder | Read |
| <a name="workdocs-GetGroup"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_Operations.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_Operations.html) | Retrieve details for the specified group | Read |
| <a name="workdocs-GetResources"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetResources.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_GetResources.html) | Get a collection of resources | Read |
| <a name="workdocs-SearchResources"></a>[https://docs.aws.amazon.com/workdocs/latest/APIReference/API_SearchResources.html](https://docs.aws.amazon.com/workdocs/latest/APIReference/API_SearchResources.html) | Search metadata and the content of resources | List |
