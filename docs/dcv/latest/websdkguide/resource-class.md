---
source_url: https://docs.aws.amazon.com/dcv/latest/websdkguide/resource-class.html
---

# Resource Class
<a name="resource-class"></a>

The Resource Class can fetch or discard the corresponding file that was just printed or downloaded. When performing these actions, the corresponding observer functions [`filePrinted`](dcv-module.md#filePrintedCallback) and [`fileDownload`](dcv-module.md#fileDownloadCallback) would respectively be invoked with the resource object as their only argument. Such resource can be accepted or declined in order to fetch or discard the file they reference.

**Topics**
+ [Methods](#methods)

## Methods
<a name="methods"></a>

**Topics**
+ [accept(urlParameters) → {void}](#accept)
+ [decline() → {void}](#decline)

### accept(urlParameters) → {void}
<a name="accept"></a>

 Locally downloads the resource.

#### Parameters:
<a name="parameters-1"></a>

|  Name  |  Type  |  Description  |
| --- | --- | --- |
|  urlParameters  |  Object  |  The optional object containing the key/value pairs of the URL search parameters passed to the request to fetch the resource.  |

#### Returns:
<a name="returns"></a>

 Type
 void

### decline() → {void}
<a name="decline"></a>

 Discards the resource.

#### Returns:
<a name="returns-1"></a>

 Type
 void

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
