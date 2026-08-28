---
source_url: https://docs.aws.amazon.com/powershell/v4/userguide/pstools-pipelines.html
---

AWS Tools for PowerShell V4 has reached end of support.

We recommend that you migrate to [AWS Tools for PowerShell V5](https://docs.aws.amazon.com/powershell/v5/userguide/). For additional details and information on how to migrate, please refer to our [end of support announcement](https://aws.amazon.com/blogs/developer/aws-tools-for-powershell-v4-end-of-support-announcement/).

# Pipelining, output, and iteration in the AWS Tools for PowerShell
<a name="pstools-pipelines"></a>

## Pipelining
<a name="pstools-pipelining"></a>

PowerShell encourages users to connect cmdlets into [pipelines](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines) that direct the output of one cmdlet into the input of the next. The following example shows this behavior when using the AWS Tools for PowerShell. The command gets and then stops all Amazon EC2 instances in the current default Region.

```
PS > Get-EC2Instance | Stop-EC2Instance
```

## Cmdlet output
<a name="pstools-output"></a>

To better support pipelining, some data from the responses of the AWS SDK for .NET might be discarded by default. The output from AWS Tools for PowerShell cmdlets isn't reshaped to include the service response and result instances as `Note` properties on the emitted collection object. Instead, for those calls that emit a single collection as output, the collection is now enumerated to the PowerShell pipeline. This means that the SDK response and result data cannot exist in the pipeline because there is no containing collection object to which it can be attached.

Although most users probably won't need this data, it can be useful for diagnostic purposes because you can see exactly what was sent to and received from the underlying AWS service calls that were made by the cmdlet. Starting with the AWS Tools for PowerShell V4, cmdlets can use the `-Select *` parameter and argument to return the entire service response.

**Note**
In versions of the AWS Tools for PowerShell prior to V4, a session variable called `$AWSHistory` was introduced that maintains a record of AWS cmdlet invocations and the service responses that were received for each invocation. In V4 of the Tools for PowerShell, this session variable was deprecated in favor of the `-Select *` parameter and argument, which can be used to return the entire service response. This parameter is described in this topic.
This is prerelease documentation for a feature in preview release. It is subject to change.
The `$AWSHistory` variable will be removed in V5 of the AWS Tools for PowerShell. For more information, see the blog post [Notice of upcoming major version 5 of AWS Tools for PowerShell](https://aws.amazon.com/blogs/developer/notice-of-upcoming-major-version-5-of-aws-tools-for-powershell/).

To illustrate how all data from a response can be returned, consider the following examples.

The first example simply returns a list of Amazon S3 buckets. This is the default behavior.

```
PS > Get-S3Bucket

CreationDate           BucketName
------------           ----------
9/22/2023 10:54:35 PM  amzn-s3-demo-bucket1
9/22/2023 11:04:37 AM  amzn-s3-demo-bucket2
9/22/2023 12:54:34 PM  amzn-s3-demo-bucket3
```

The second example returns an AWS SDK for .NET response object. Because `-Select *` was specified, the output includes the entire API response, which contains the collection of buckets in the `Buckets` property. In this example, the `Format-List` cmdlet isn't strictly necessary, but is present to ensure that all properties are displayed.

```
PS > Get-S3Bucket -Select * | Format-List

LoggedAt          : 10/1/2023 9:45:52 AM
Buckets           : {amzn-s3-demo-bucket1, amzn-s3-demo-bucket2,
                    amzn-s3-demo-bucket3}
Owner             : Amazon.S3.Model.Owner
ContinuationToken :
ResponseMetadata  : Amazon.Runtime.ResponseMetadata
ContentLength     : 0
HttpStatusCode    : OK
```

## Iteration through paged data
<a name="pstools-iteration"></a>

The following sections describe various types of iteration that are possible.

### Automatic iteration
<a name="pstools-iteration-auto"></a>

For service APIs that impose a default maximum number of returned objects for a given call or that support pageable result sets, most cmdlets implement automatic iteration, which enables the default behavior of "page-to-completion". In this scenario, a cmdlet makes as many calls as necessary on your behalf to return the complete data set to the pipeline.

In the following example, which uses the `Get-S3Object` cmdlet, the `$result` variable contains `S3Object` instances for every key in a bucket called `amzn-s3-demo-bucket1`, which is potentially a very large data set.

```
PS > $result = Get-S3Object -BucketName amzn-s3-demo-bucket1
```

The following example reduces the number of results for each page during automatic iteration from the default value of 1000 to 500. The example performs twice as many automatic iteration calls because only half as many results are returned for each call.

```
PS > $result = Get-S3Object -BucketName amzn-s3-demo-bucket1 -MaxKey 500
```

**Note**
In the AWS Tools for PowerShell V4, some cmdlets for paged operations don't implement automatic iteration. If a cmdlet doesn't have the `-NoAutoIteration` parameter, which is discussed in the next section, then it doesn't implement automatic iteration.

### Disable automatic iteration
<a name="pstools-iteration-disable-auto"></a>

If you want the Tools for PowerShell to return only the first page of data, you can add the `-NoAutoIteration` parameter to prevent additional pages of data from being returned.

The following example uses the `-NoAutoIteration` and `-MaxKey` parameters to limit the number of returned `S3Object` instances to no more than the first 500 found in the bucket.

```
PS > $result = Get-S3Object -BucketName amzn-s3-demo-bucket1 -MaxKey 500 -NoAutoIteration
```

To determine if more data was available but not returned, use the `-Select *` parameter and argument and check if there is a value in the next token property.

The following example returns `$true` if there are more than 500 objects in the bucket and `$false` otherwise.

```
PS > $result = Get-S3Object -BucketName amzn-s3-demo-bucket1 -MaxKey 500 -NoAutoIteration -Select *
PS > $null -eq $result.NextMarker
```

**Note**
The names of the next token response property and cmdlet parameter vary between cmdlets. For details, refer to the help documentation for each cmdlet.

### Manual iteration
<a name="pstools-iteration-manual"></a>

The following example returns all S3 objects from a bucket using a [do](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_do) loop, which evaluates the condition after each iteration. The `do` loop performs iterations until `Get-S3Object` sets `$result.NextMarker` to `$null`, indicating that no more paged data remains. The output of the loop is assigned to the `$s3Objects` variable.

```
$s3Objects = do
{
    $splatParams = @{
        BucketName = 'amzn-s3-demo-bucket1'
        MaxKey = 500
        Marker = $result.NextMarker
        NoAutoIteration = $true
        Select = '*'
    }
    $result = Get-S3Object @splatParams

    $result.S3Objects
}
while ($null -ne $result.NextMarker)
```

This example uses PowerShell [splatting](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting) to avoid a long line of code that would be caused by declaring parameters and arguments in-line.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
