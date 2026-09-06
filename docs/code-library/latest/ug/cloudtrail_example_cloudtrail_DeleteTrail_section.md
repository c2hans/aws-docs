---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudtrail_example_cloudtrail_DeleteTrail_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteTrail` with an AWS SDK or CLI
<a name="cloudtrail_example_cloudtrail_DeleteTrail_section"></a>

The following code examples show how to use `DeleteTrail`.

------
#### [ C\+\+ ]

**SDK for C\+\+**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/cloudtrail#code-examples).

```
// Routine which deletes an AWS CloudTrail trail.
/*!
  \param trailName: The name of the CloudTrail trail.
  \param clientConfig: Aws client configuration.
  \return bool: Function succeeded.
*/
bool AwsDoc::CloudTrail::deleteTrail(const Aws::String trailName,
                                     const Aws::Client::ClientConfiguration &clientConfig) {
    Aws::CloudTrail::CloudTrailClient trailClient(clientConfig);

    Aws::CloudTrail::Model::DeleteTrailRequest request;
    request.SetName(trailName);

    auto outcome = trailClient.DeleteTrail(request);
    if (outcome.IsSuccess()) {
        std::cout << "Successfully deleted trail " << trailName << std::endl;
    }
    else {
        std::cerr << "Error deleting trail " << trailName << " " <<
                  outcome.GetError().GetMessage() << std::endl;
    }

    return outcome.IsSuccess();
}
```
+  For API details, see [DeleteTrail](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/DeleteTrail) in *AWS SDK for C\+\+ API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To delete a trail**
The following `delete-trail` command deletes a trail named `Trail1`:

```
aws cloudtrail delete-trail --name {{Trail1}}
```
+  For API details, see [DeleteTrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/delete-trail.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Deletes the specified trail. You will be prompted for confirmation before the command is run. To suppress confirmation, add the -Force switch parameter.**

```
Remove-CTTrail -Name "awscloudtrail-example"
```
+  For API details, see [DeleteTrail](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Deletes the specified trail. You will be prompted for confirmation before the command is run. To suppress confirmation, add the -Force switch parameter.**

```
Remove-CTTrail -Name "awscloudtrail-example"
```
+  For API details, see [DeleteTrail](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
#### [ Ruby ]

**SDK for Ruby**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/ruby/example_code/cloudtrail#code-examples).

```
  client.delete_trail({
                        name: trail_name # required
                      })
  puts "Successfully deleted trail: #{trail_name}"
rescue StandardError => e
  puts "Got error trying to delete trail: #{trail_name}:"
  puts e
  exit 1
end
```
+  For API details, see [DeleteTrail](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/DeleteTrail) in *AWS SDK for Ruby API Reference*.

------
