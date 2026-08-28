---
source_url: https://docs.aws.amazon.com/parallelcluster/latest/ug/list-official-images.html
---

# listOfficialImages
<a name="list-official-images"></a>

Retrieve the list of AWS ParallelCluster official images.

**Topics**
+ [Request syntax](#list-official-images-request)
+ [Request body](#list-official-images-request-body)
+ [Response syntax](#list-official-images-response)
+ [Response body](#list-official-images-response-body)
+ [Example](#list-official-images-example)

## Request syntax
<a name="list-official-images-request"></a>

```
GET /v3/images/official
{
  "architecture": "string",
  "os": "string",
  "region": "string"
}
```

## Request body
<a name="list-official-images-request-body"></a>

**architecture**
Filter by architecture. The default is no filtering.
Type: string
Valid values: `x86_64 | arm64`
Required: No

**os**
Filter by OS distribution. The default is no filtering.
Type: string
Valid values: `alinux2023 | ubuntu2404 | ubuntu2204 | rhel8 | rhel9`
Required: No

**region**
The AWS Region in which official images are listed.
Type: string
Required: No

## Response syntax
<a name="list-official-images-response"></a>

```
{
  "images": [
    {
      "architecture": "string",
      "amiId": "string",
      "name": "string",
      "os": "string",
      "version": "string"
    }
  ]
}
```

## Response body
<a name="list-official-images-response-body"></a>

**images**
**amiId**
The ID of the AMI.
Type: string
**architecture**
The AMI architecture.
Type: string
**name**
The name of the AMI.
Type: string
**os**
The AMI operating system.
Type: string
**version**
The AWS ParallelCluster version.
Type: string

## Example
<a name="list-official-images-example"></a>

------
#### [ Python ]

**Request**

```
$ list_official_images()
```

**200 Response**

```
{
  'images': [
    {
      'ami_id': 'ami-015cfeb4e0d6306b2',
      'architecture': 'x86_64',
      'name': 'aws-parallelcluster-3.2.1-ubuntu-2204-lts-hvm-x86_64-202202261505 '
      '2022-02-26T15-08-34.759Z',
      'os': 'ubuntu2204',
      'version': '3.2.1'
    },
    ...
  ]
}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS ParallelCluster. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query parallelcluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
