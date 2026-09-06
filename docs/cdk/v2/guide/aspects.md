---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/aspects.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Aspects and the AWS CDK
<a name="aspects"></a>

Aspects are a way to apply an operation to all constructs in a given scope. The aspect could modify the constructs, such as by adding tags. Or it could verify something about the state of the constructs, such as making sure that all buckets are encrypted.

To apply an aspect to a construct and all constructs in the same scope, call ` [Aspects](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.Aspects.html#static-ofscope).of(<SCOPE>).add()` with a new aspect, as shown in the following example.

**Example**

```
Aspects.of(myConstruct).add(new SomeAspect(...));
```

```
Aspects.of(myConstruct).add(new SomeAspect(...));
```

```
Aspects.of(my_construct).add(SomeAspect(...))
```

```
Aspects.of(myConstruct).add(new SomeAspect(...));
```

```
Aspects.Of(myConstruct).add(new SomeAspect(...));
```

```
awscdk.Aspects_Of(stack).Add(awscdk.NewTag(...))
```

The AWS CDK uses aspects to [tag resources](tagging.md), but the framework can also be used for other purposes. For example, you can use it to validate or change the AWS CloudFormation resources that are defined for you by higher-level constructs.

## Aspects vs. Mixins
<a name="aspects-vs-mixins"></a>

Aspects and [Mixins](mixins.md) both modify constructs, but they differ in when and how they are applied:

| Feature | Aspects | Mixins |
| --- | --- | --- |
|  **When applied**  | During synthesis, after all other code has run. | Immediately when `.with()` is called. |
|  **Scope**  | All constructs in a given scope, including constructs added later. | Only the constructs you explicitly apply them to. |
|  **Style**  | Declarative — you set a rule and the CDK applies it. | Imperative — you choose what to apply and where. |
|  **Best for**  | Validation, compliance, tagging, broad policies. | Adding specific features to individual resources. |

Use Aspects when you want to enforce rules across your entire application or validate that constructs meet certain criteria. Use Mixins when you want to add a specific feature to a specific construct.

Aspects and Mixins can be used together. For example, you might use Mixins to configure individual resources and Aspects to validate that all resources in a stack meet your organization’s security requirements.

## Aspects in detail
<a name="aspects-detail"></a>

Aspects employ the [visitor pattern](https://en.wikipedia.org/wiki/Visitor_pattern). An aspect is a class that implements the following interface.

**Example**

```
interface IAspect {
   visit(node: IConstruct): void;}
```
JavaScript doesn’t have interfaces as a language feature. Therefore, an aspect is simply an instance of a class having a `visit` method that accepts the node to be operated on.
Python doesn’t have interfaces as a language feature. Therefore, an aspect is simply an instance of a class having a `visit` method that accepts the node to be operated on.

```
public interface IAspect {
    public void visit(Construct node);
}
```

```
public interface IAspect
{
    void Visit(IConstruct node);
}
```

```
type IAspect interface {
  Visit(node constructs.IConstruct)
}
```

When you call `Aspects.of(<SCOPE>).add(…​)`, the construct adds the aspect to an internal list of aspects. You can obtain the list with `Aspects.of(<SCOPE>)`.

During the [prepare phase](deploy.md#deploy-how-synth-app), the AWS CDK calls the `visit` method of the object for the construct and each of its children in top-down order.

The `visit` method is free to change anything in the construct. In strongly typed languages, cast the received construct to a more specific type before accessing construct-specific properties or methods.

Aspects don’t propagate across `Stage` construct boundaries, because `Stages` are self-contained and immutable after definition. Apply aspects on the `Stage` construct itself (or lower) if you want them to visit constructs inside the `Stage`.

## Example
<a name="aspects-example"></a>

The following example validates that all buckets created in the stack have versioning enabled. The aspect adds an error annotation to the constructs that fail the validation. This results in the `synth` operation failing and prevents deploying the resulting cloud assembly.

**Example**

```
class BucketVersioningChecker implements IAspect {
  public visit(node: IConstruct): void {
    // See that we're dealing with a CfnBucket
    if (node instanceof s3.CfnBucket) {

      // Check for versioning property, exclude the case where the property
      // can be a token (IResolvable).
      if (!node.versioningConfiguration
        || (!Tokenization.isResolvable(node.versioningConfiguration)
            && node.versioningConfiguration.status !== 'Enabled')) {
        Annotations.of(node).addError('Bucket versioning is not enabled');
      }
    }
  }
}

// Later, apply to the stack
Aspects.of(stack).add(new BucketVersioningChecker());
```

```
class BucketVersioningChecker {
   visit(node) {
    // See that we're dealing with a CfnBucket
    if ( node instanceof s3.CfnBucket) {

      // Check for versioning property, exclude the case where the property
      // can be a token (IResolvable).
      if (!node.versioningConfiguration
        || !Tokenization.isResolvable(node.versioningConfiguration)
            && node.versioningConfiguration.status !== 'Enabled')) {
        Annotations.of(node).addError('Bucket versioning is not enabled');
      }
    }
  }
}

// Later, apply to the stack
Aspects.of(stack).add(new BucketVersioningChecker());
```

```
@jsii.implements(cdk.IAspect)
class BucketVersioningChecker:

  def visit(self, node):
    # See that we're dealing with a CfnBucket
    if isinstance(node, s3.CfnBucket):

      # Check for versioning property, exclude the case where the property
      # can be a token (IResolvable).
      if (not node.versioning_configuration or
              not Tokenization.is_resolvable(node.versioning_configuration)
                  and node.versioning_configuration.status != "Enabled"):
          Annotations.of(node).add_error('Bucket versioning is not enabled')

# Later, apply to the stack
Aspects.of(stack).add(BucketVersioningChecker())
```

```
public class BucketVersioningChecker implements IAspect
{
    @Override
    public void visit(Construct node)
    {
        // See that we're dealing with a CfnBucket
        if (node instanceof CfnBucket)
        {
            CfnBucket bucket = (CfnBucket)node;
            Object versioningConfiguration = bucket.getVersioningConfiguration();
            if (versioningConfiguration == null ||
                    !Tokenization.isResolvable(versioningConfiguration.toString()) &&
                    !versioningConfiguration.toString().contains("Enabled"))
                Annotations.of(bucket.getNode()).addError("Bucket versioning is not enabled");
        }
    }
}

// Later, apply to the stack
Aspects.of(stack).add(new BucketVersioningChecker());
```

```
class BucketVersioningChecker : Amazon.Jsii.Runtime.Deputy.DeputyBase, IAspect
{
    public void Visit(IConstruct node)
    {
        // See that we're dealing with a CfnBucket
        if (node is CfnBucket)
        {
            var bucket = (CfnBucket)node;
            if (bucket.VersioningConfiguration is null ||
                    !Tokenization.IsResolvable(bucket.VersioningConfiguration) &&
                    !bucket.VersioningConfiguration.ToString().Contains("Enabled"))
                Annotations.Of(bucket.Node).AddError("Bucket versioning is not enabled");
        }
    }
}

// Later, apply to the stack
Aspects.Of(stack).add(new BucketVersioningChecker());
```
