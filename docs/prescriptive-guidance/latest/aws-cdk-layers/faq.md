---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-cdk-layers/faq.html
---

# FAQ
<a name="faq"></a>

**Can't I use the AWS CDK without understanding layers?**

You absolutely can. But as with most powerful tools, the AWS CDK becomes more powerful the more you know about it. Learning how the AWS CDK's layers interact unlocks a new level of understanding that helps simplify your stack deployments far beyond what you can do with just basic AWS CDK knowledge.

**Can I make L2 constructs from L1 in the same way that I make L3 constructs from L2?**

If a resource already has an L2 construct, we recommend that you use that construct and make your customizations in layer 3. This is because much research has already gone into figuring out the best ways to configure existing L2 constructs for a particular resource. However, there are several L1 constructs whose L2 constructs don't exist yet. In those cases, we encourage you to create your own L2 constructs and share them with others by becoming a contributor to the AWS CDK open source library. You can find everything you need to get started in the [contribution guidelines](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) for the AWS CDK.

**Which AWS resources don't yet have official L2 constructs?**

The number of AWS resources that don't have L2 constructs is getting lower by the day, but if you're interested in helping create an L2 construct for one of these resources, visit the [AWS CDK API Reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html). Look at the list of resources in the left pane. The resources that have the superscript 1 next to their names don't have official L2 constructs.

**Can I make an L2 or L3 construct in any language that the AWS CDK supports?**

The AWS CDK supports several programming languages, including TypeScript, JavaScript, Python, Java, C\#, and Go. You can create your personal L3 constructs by using the AWS CDK code compiled into the relevant language. However, if you want to contribute to the AWS CDK or create native AWS CDK constructs, you must use TypeScript. This is because TypeScript is the only language that is native to the AWS CDK. The AWS CDK versions for other languages are built from the native TypeScript code by using an AWS library called [JSii](https://github.com/aws/jsii).

**Where can I find existing L3 constructs outside of the AWS CDK?**

There are too many locations to share here, but you can find many of the most popular constructs on the [AWS Solutions Constructs](https://aws.amazon.com/solutions/constructs/) website and in the AWS CDK section of the [Construct Hub](https://constructs.dev/search?q=&cdk=aws-cdk&cdkver=2&sort=downloadsDesc&offset=0).
