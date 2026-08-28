---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/asff-resourcedetails-container.html
---

# Container object in ASFF
<a name="asff-resourcedetails-container"></a>

The following example shows the AWS Security Finding Format (ASFF) syntax for the `Container` object. To view descriptions of `Container` attributes, see [ContainerDetails](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ContainerDetails.html) in the *AWS Security Hub API Reference*. For background information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md).

**Example**

```
"Container": {
    "ContainerRuntime": "docker",
    "ImageId": "image12",
    "ImageName": "1111111/knotejs@sha256:372131c9fef111111111111115f4ed3ea5f9dce4dc3bd34ce21846588a3",
    "LaunchedAt": "2018-09-29T01:25:54Z",
    "Name": "knote",
    "Privileged": true,
    "VolumeMounts": [{
        "Name": "vol-03909e9",
        "MountPath": "/mnt/etc"
    }]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
