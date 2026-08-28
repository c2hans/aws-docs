---
source_url: https://docs.aws.amazon.com/vm-import/latest/userguide/start-image-export.html
---

# Start an export image task
<a name="start-image-export"></a>

When you export your image using VM Import/Export, the exported file is written to the specified S3 bucket using the following S3 key:

```
{{prefix}}export-ami-{{xxxxxxxxxxxxxxxxx}}.{{format}}
```

For example, if the bucket name is `amzn-s3-demo-export-bucket`, the prefix is `exports/`, and the format is VMDK, the exported image is written to `amzn-s3-demo-export-bucket/exports/export-ami-1234567890abcdef0.vmdk`.

For information about the supported formats, see [Considerations for image export](limits-image-export.md).

------
#### [ AWS CLI ]

**To export an image**
Use the [export-image](https://docs.aws.amazon.com/cli/latest/reference/ec2/export-image.html) command.

```
aws ec2 export-image \
    --description "$(date '+%b %d %H:%M') My image export" \
    --image-id {{ami-1234567890abcdef0}} \
    --disk-image-format {{VMDK}} \
    --s3-export-location S3Bucket={{amzn-s3-demo-export-bucket}},S3Prefix={{exports/}}
```

The following is example output.

```
{
    "Description": "Jul 15 16:31 My image export",
    "DiskImageFormat": "VMDK",
    "ExportImageTaskId": "export-ami-36a041c1000000000",
    "ImageId": "ami-1234567890abcdef0",
    "Progress": "0",
    "S3ExportLocation": {
        "S3Bucket": "amzn-s3-demo-export-bucket",
        "S3Prefix": "exports/"
    },
    "Status": "active",
    "StatusMessage": "validating"
}
```

------
#### [ PowerShell ]

**To export an image**
Use the [Export-EC2Image](https://docs.aws.amazon.com/powershell/latest/reference/items/Export-EC2Image.html) cmdlet.

```
Export-EC2Image `
    -Description ((Get-Date -Format "MMM dd HH:mm ") + "My image export") `
    -ImageId {{ami-1234567890abcdef0}} `
    -DiskImageFormat VMDK `
    -S3ExportLocation_S3Bucket {{amzn-s3-demo-export-bucket}} `
    -S3ExportLocation_S3Prefix {{exports/}}
```

The following is example output.

```
Description       : Jul 15 16:35 My image export
DiskImageFormat   : VMDK
ExportImageTaskId : export-ami-36a041c1000000000
ImageId           : ami-1234567890abcdef0
Progress          : 0
RoleName          :
S3ExportLocation  : Amazon.EC2.Model.ExportTaskS3Location
Status            : active
StatusMessage     : validating
Tags              : {}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query vm-import` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
