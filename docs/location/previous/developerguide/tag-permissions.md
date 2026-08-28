---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/tag-permissions.html
---

# Grant permission to tag resources
<a name="tag-permissions"></a>

You can use IAM policies to control access to your Amazon Location resources and grant permission to tag a resource on creation. In addition to granting permission to create resources, the policy can include `Action` permissions to allow tagging operations:
+ `geo:TagResource` – Allows a user to assign one or more tags to a specified Amazon Location resource.
+ `geo:UntagResource` – Allows a user to remove one or more tags from a specified Amazon Location resource.
+ `geo:ListTagsForResource` – Allows a user to list all the tags assigned to an Amazon Location resource.

The following is a policy example to allow a user to create a geofence collection and tag resources:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowTaggingForGeofenceCollectionOnCreation",
            "Effect": "Allow",
            "Action": [
                "geo:CreateGeofenceCollection",
                "geo:TagResource"
            ],
            "Resource": "arn:aws:geo:{{region}}:{{accountID}}:geofence-collection/*"
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
