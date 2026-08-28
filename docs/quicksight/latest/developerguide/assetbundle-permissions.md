---
source_url: https://docs.aws.amazon.com/quicksight/latest/developerguide/assetbundle-permissions.html
---

# Permissions
<a name="assetbundle-permissions"></a>

Before you begin, verify that you have an AWS Identity and Access Management role that grants the CLI user access to call the Quick Sight asset bundle API operations.

Quick Sight recommends that you use the `AWSQuickSightAssetBundleExportPolicy` and `AWSQuickSightAssetBundleImportPolicy` IAM managed policies to streamline your API usage. You can also choose to explicitly define your oen IAM policy to fit your use case. For more information about IAM managed policies in Quick Sight, see [AWS managed policies for Quick Sight](https://docs.aws.amazon.com/quicksight/latest/user/security-iam-quicksight.html).

The following example shows an IAM policy that you can add to an existing IAM role to use the `StartAssetBundleExportJob` operation.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "quicksight:DescribeAssetBundleExportJob",
        "quicksight:ListAssetBundleExportJobs",
        "quicksight:StartAssetBundleExportJob",
        "quicksight:DescribeAnalysis",
        "quicksight:DescribeDashboard",
        "quicksight:DescribeDataSet",
        "quicksight:DescribeDataSetRefreshProperties",
        "quicksight:DescribeDataSource",
        "quicksight:DescribeRefreshSchedule",
        "quicksight:DescribeTheme",
        "quicksight:DescribeVPCConnection",
        "quicksight:ListRefreshSchedules",
        "quicksight:DescribeAnalysisPermissions",
        "quicksight:DescribeDashboardPermissions",
        "quicksight:DescribeDataSetPermissions",
        "quicksight:DescribeDataSourcePermissions",
        "quicksight:DescribeThemePermissions",
        "quicksight:ListTagsForResource"
      ],
      "Resource": "*"
    }
  ]
}
```

------

The following example shows an IAM policy that you can add to an existing IAM role to use the `StartAssetBundleImportJob` operation.

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
      {
        "Effect": "Allow",
        "Action": [
            "quicksight:DescribeAssetBundleImportJob",
            "quicksight:ListAssetBundleImportJobs",
            "quicksight:StartAssetBundleImportJob",
            "quicksight:CreateAnalysis",
            "quicksight:DeleteAnalysis",
            "quicksight:DescribeAnalysis",
            "quicksight:UpdateAnalysis",
            "quicksight:CreateDashboard",
            "quicksight:DeleteDashboard",
            "quicksight:DescribeDashboard",
            "quicksight:UpdateDashboard",
            "quicksight:UpdateDashboardLinks",
            "quicksight:UpdateDashboardPublishedVersion",
            "quicksight:CreateDataSet",
            "quicksight:DeleteDataSet",
            "quicksight:DescribeDataSet",
            "quicksight:PassDataSet",
            "quicksight:UpdateDataSet",
            "quicksight:DeleteDataSetRefreshProperties",
            "quicksight:DescribeDataSetRefreshProperties",
            "quicksight:PutDataSetRefreshProperties",
            "quicksight:CreateRefreshSchedule",
            "quicksight:DescribeRefreshSchedule",
            "quicksight:DeleteRefreshSchedule",
            "quicksight:ListRefreshSchedules",
            "quicksight:UpdateRefreshSchedule",
            "quicksight:CreateDataSource",
            "quicksight:DescribeDataSource",
            "quicksight:DeleteDataSource",
            "quicksight:PassDataSource",
            "quicksight:UpdateDataSource",
            "quicksight:CreateTheme",
            "quicksight:DeleteTheme",
            "quicksight:DescribeTheme",
            "quicksight:UpdateTheme",
            "quicksight:CreateVPCConnection",
            "quicksight:DescribeVPCConnection",
            "quicksight:DeleteVPCConnection",
            "quicksight:UpdateVPCConnection",
            "quicksight:DescribeAnalysisPermissions",
            "quicksight:DescribeDashboardPermissions",
            "quicksight:DescribeDataSetPermissions",
            "quicksight:DescribeDataSourcePermissions",
            "quicksight:DescribeThemePermissions",
            "quicksight:UpdateAnalysisPermissions",
            "quicksight:UpdateDashboardPermissions",
            "quicksight:UpdateDataSetPermissions",
            "quicksight:UpdateDataSourcePermissions",
            "quicksight:UpdateThemePermissions",
            "quicksight:ListTagsForResource",
            "quicksight:TagResource",
            "quicksight:UntagResource",
            "s3:GetObject",
            "iam:PassRole"
        ],
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "iam:PassedToService": "quicksight.amazonaws.com"
            }
        }
      }
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
