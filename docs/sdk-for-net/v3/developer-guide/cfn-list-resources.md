---
source_url: https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/cfn-list-resources.html
---

The AWS SDK for .NET V3 has reached end-of-support.

We recommend that you migrate to [AWS SDK for .NET V4](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/welcome.html). For additional details and information on how to migrate, please refer to our [end-of-support announcement](https://aws.amazon.com/blogs/developer/aws-sdk-for-net-v3-end-of-support-announcement/).

# Listing AWS resources using AWS CloudFormation
<a name="cfn-list-resources"></a>

This example shows you how to use the AWS SDK for .NET to list the resources in CloudFormation stacks. The example uses the low-level API. The application takes no arguments, but simply gathers information for all stacks that are accessible to the user's credentials and then displays information about those stacks.

## SDK references
<a name="w2aac19c15c11c13b5b1"></a>

NuGet packages:
+ [AWSSDK.CloudFormation](https://www.nuget.org/packages/AWSSDK.CloudFormation/)

Programming elements:
+ Namespace [Amazon.CloudFormation](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/CloudFormation/NCloudFormation.html)

  Class [AmazonCloudFormationClient](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/CloudFormation/TCloudFormationClient.html)
+ Namespace [Amazon.CloudFormation.Model](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/CloudFormation/NCloudFormationModel.html)

  Class [ICloudFormationPaginatorFactory.DescribeStacks](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/CloudFormation/MICloudFormationPaginatorFactoryDescribeStacksDescribeStacksRequest.html)

  Class [DescribeStackResourcesRequest](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/CloudFormation/TDescribeStackResourcesRequest.html)

  Class [DescribeStackResourcesResponse](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/CloudFormation/TDescribeStackResourcesResponse.html)

  Class [Stack](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/CloudFormation/TStack.html)

  Class [StackResource](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/CloudFormation/TStackResource.html)

  Class [Tag](https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/CloudFormation/TTag.html)

```
using Amazon.CloudFormation;
using Amazon.CloudFormation.Model;
using Amazon.Runtime;

namespace CloudFormationActions;

public static class HelloCloudFormation
{
    public static IAmazonCloudFormation _amazonCloudFormation;

    static async Task Main(string[] args)
    {
        // Create the CloudFormation client
        _amazonCloudFormation = new AmazonCloudFormationClient();
        Console.WriteLine($"\nIn Region: {_amazonCloudFormation.Config.RegionEndpoint}");

        // List the resources for each stack
        await ListResources();
    }

    /// <summary>
    /// Method to list stack resources and other information.
    /// </summary>
    /// <returns>True if successful.</returns>
    public static async Task<bool> ListResources()
    {
        try
        {
            Console.WriteLine("Getting CloudFormation stack information...");

            // Get all stacks using the stack paginator.
            var paginatorForDescribeStacks =
                _amazonCloudFormation.Paginators.DescribeStacks(
                    new DescribeStacksRequest());
            await foreach (Stack stack in paginatorForDescribeStacks.Stacks)
            {
                // Basic information for each stack
                Console.WriteLine("\n------------------------------------------------");
                Console.WriteLine($"\nStack: {stack.StackName}");
                Console.WriteLine($"  Status: {stack.StackStatus.Value}");
                Console.WriteLine($"  Created: {stack.CreationTime}");

                // The tags of each stack (etc.)
                if (stack.Tags.Count > 0)
                {
                    Console.WriteLine("  Tags:");
                    foreach (Tag tag in stack.Tags)
                        Console.WriteLine($"    {tag.Key}, {tag.Value}");
                }

                // The resources of each stack
                DescribeStackResourcesResponse responseDescribeResources =
                    await _amazonCloudFormation.DescribeStackResourcesAsync(
                        new DescribeStackResourcesRequest
                        {
                            StackName = stack.StackName
                        });
                if (responseDescribeResources.StackResources.Count > 0)
                {
                    Console.WriteLine("  Resources:");
                    foreach (StackResource resource in responseDescribeResources
                                 .StackResources)
                        Console.WriteLine(
                            $"    {resource.LogicalResourceId}: {resource.ResourceStatus}");
                }
            }

            Console.WriteLine("\n------------------------------------------------");
            return true;
        }
        catch (AmazonCloudFormationException ex)
        {
            Console.WriteLine("Unable to get stack information:\n" + ex.Message);
            return false;
        }
        catch (AmazonServiceException ex)
        {
            if (ex.Message.Contains("Unable to get IAM security credentials"))
            {
                Console.WriteLine(ex.Message);
                Console.WriteLine("If you are usnig SSO, be sure to install" +
                                  " the AWSSDK.SSO and AWSSDK.SSOOIDC packages.");
            }
            else
            {
                Console.WriteLine(ex.Message);
                Console.WriteLine(ex.StackTrace);
            }

            return false;
        }
        catch (ArgumentNullException ex)
        {
            if (ex.Message.Contains("Options property cannot be empty: ClientName"))
            {
                Console.WriteLine(ex.Message);
                Console.WriteLine("If you are using SSO, have you logged in?");
            }
            else
            {
                Console.WriteLine(ex.Message);
                Console.WriteLine(ex.StackTrace);
            }

            return false;
        }
    }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for .NET. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-net` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
