---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/userguide/tag-resources.html
---

# Tag Image Builder output resources

Tagging your resources can be useful for filtering and tracking resource costs, or other categories. You can also control access based on tags. For more information about tag-based authorization, see [Authorization based on Image Builder tags](security_iam_service-with-iam.md#security-iam-service-with-ib-tags)

In a distribution configuration, you can use dynamic tags in the output AMI name, the AMI description, and AMI tag values for AMIs, and in the container image description and container tags for container builds. Image Builder resolves them when it creates the output resources for a build. For more information about distribution settings, see [Manage Image Builder distribution settings](manage-distribution-settings.md).

Image Builder supports the following dynamic tags:
+ `{{imagebuilder:buildDate}}`

  Resolves to the start date and time of the build, as an ISO 8601 timestamp. For example, `2026-11-24T16:40:25.000Z`.

  To control the timestamp format, append a format string to the tag. For example, `{{imagebuilder:buildDate:yyyyMMdd}}` resolves to `20261124`. The format can combine the `yyyy` (year), `MM` (month), `dd` (day), `HH` (hour), `mm` (minute), and `ss` (second) specifiers. The other dynamic tags don't support a format.
+ `{{imagebuilder:buildVersion}}`

  Resolves to the build version, which is the number at the end of the image's Amazon Resource Name (ARN). For example, the image ARN `arn:aws:imagebuilder:{{us-west-2}}:{{111122223333}}:image/{{my-example-image}}/{{1.0.0/7}}` resolves the build version to `7`.
+ `{{imagebuilder:imageName}}`

  Resolves to the name of the image resource.
+ `{{imagebuilder:imageVersion}}`

  Resolves to the semantic version of the image, for example `1.0.0`. It doesn't include the build version number.

The following example shows dynamic tags in the `amiDistributionConfiguration` of a `CreateDistributionConfiguration` request:

```json
{
    "name": "my-example-distribution",
    "distributions": [
        {
            "region": "us-west-2",
            "amiDistributionConfiguration": {
                "name": "my-image {{imagebuilder:buildDate}}",
                "amiTags": {
                    "SourceImageName": "{{imagebuilder:imageName}}",
                    "SourceImageVersion": "{{imagebuilder:imageVersion}}/{{imagebuilder:buildVersion}}"
                }
            }
        }
    ]
}
```

**Note**
In a resolved AMI name, Image Builder replaces each colon with a hyphen, because colons aren't valid in AMI names. For example, the AMI name in the preceding request resolves to `my-image 2026-11-24T16-40-25.000Z`. In a resolved container tag, Image Builder replaces both colons and spaces with hyphens. These replacements apply to the whole resolved field value, not just the text that a dynamic tag resolves to. Image Builder doesn't change description fields or AMI tag values.

To help you keep track of Amazon Machine Images (AMIs) that you've distributed, Image Builder automatically adds the following tags to your output AMIs.
+ `"CreatedBy":"EC2 Image Builder"`
+ `"Ec2ImageBuilderArn":"arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image/{{simple-recipe-linux}}/{{1.0.0/10}}"`. This tag contains the ARN of the Image Builder image resource that was used to create the AMI.

**Topics**
+ [Tag a resource](#cli-tag-resource)
+ [Untag a resource](#cli-untag-resource)
+ [List the tags for a resource](#cli-list-tags-for-resource)

## Tag a resource
<a name="cli-tag-resource"></a>

------
#### [ AWS CLI ]

The following example shows how to add tags to a resource in EC2 Image Builder. You must provide the `resourceArn` and the tags to apply to it.

The example `tag-resource.json` contents are as follows:

```json
{
    "resourceArn": "arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}}",
    "tags": {
        "KeyName": "KeyValue"
    }
}
```

Run the following command, which references the preceding `tag-resource.json` file.

```
aws imagebuilder tag-resource --cli-input-json file://tag-resource.json
```

------
#### [ PowerShell ]

The following example shows how to use the [Add-EC2IBResourceTag](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-EC2IBResourceTag.html) cmdlet to add tags to a resource by specifying its Amazon Resource Name (ARN):

```ps
Add-EC2IBResourceTag -ResourceArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}} `
    -Tag @{{{KeyName}}="{{KeyValue}}"}
```

------

## Untag a resource
<a name="cli-untag-resource"></a>

------
#### [ AWS CLI ]

The following example shows how to remove a tag from a resource. You must provide the `resourceArn` and the keys to remove the tag.

The example `untag-resource.json` contents are as follows:

```json
{
    "resourceArn": "arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}}",
    "tagKeys": [
        "KeyName"
    ]
}
```

Run the following command, which references the preceding `untag-resource.json` file.

```
aws imagebuilder untag-resource --cli-input-json file://untag-resource.json
```

------
#### [ PowerShell ]

The following example shows how to use the [Remove-EC2IBResourceTag](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2IBResourceTag.html) cmdlet to remove a tag from a resource by specifying its Amazon Resource Name (ARN):

```ps
Remove-EC2IBResourceTag -ResourceArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}} `
    -TagKey {{KeyName}}
```

------

## List the tags for a resource
<a name="cli-list-tags-for-resource"></a>

------
#### [ AWS CLI ]

The following example shows how to list all the tags for a specific resource.

```
aws imagebuilder list-tags-for-resource --resource-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}}
```

------
#### [ PowerShell ]

The following example shows how to use the [Get-EC2IBResourceTag](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IBResourceTag.html) cmdlet to list all the tags for a specific resource by specifying its Amazon Resource Name (ARN):

```ps
Get-EC2IBResourceTag -ResourceArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}}
```

------
