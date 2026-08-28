---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-go.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Working with the AWS CDK in Go
<a name="work-with-cdk-go"></a>

 Go is a fully-supported client language for the AWS Cloud Development Kit (AWS CDK) and is considered stable. Working with the AWS CDK in Go uses familiar tools. The Go version of the AWS CDK even uses Go-style identifiers.

Unlike the other languages the CDK supports, Go is not a traditional object-oriented programming language. Go uses composition where other languages often leverage inheritance. We have tried to employ idiomatic Go approaches as much as possible, but there are places where the CDK may differ.

This topic provides guidance when working with the AWS CDK in Go. See the [announcement blog post](https://aws.amazon.com/blogs/developer/getting-started-with-the-aws-cloud-development-kit-and-go/) for a walkthrough of a simple Go project for the AWS CDK.

## Get started with Go
<a name="go-prerequisites"></a>

To work with the AWS CDK, you must have an AWS account and credentials and have installed Node.js and the AWS CDK Toolkit. See [Getting started with the AWS CDK](getting-started.md).

The Go bindings for the AWS CDK use the standard [Go toolchain](https://golang.org/dl/), v1.23 or later. You can use the editor of your choice.

**Note**
Third-party language deprecation: language version is only supported until its EOL (End Of Life) shared by the vendor or community and is subject to change with prior notice.

## Creating a project
<a name="go-newproject"></a>

You create a new AWS CDK project by invoking `cdk init` in an empty directory. Use the `--language` option and specify `go`:

```
mkdir my-project
cd my-project
cdk init app --language go
```

 `cdk init` uses the name of the project folder to name various elements of the project, including classes, subfolders, and files. Hyphens in the folder name are converted to underscores. However, the name should otherwise follow the form of a Go identifier; for example, it should not start with a number or contain spaces.

The resulting project includes a reference to the core AWS CDK Go module, `github.com/aws/aws-cdk-go/awscdk/v2`, in `go.mod`. Issue `go get` to install this and other required modules.

## Managing AWS Construct Library modules
<a name="go-managemodules"></a>

In most AWS CDK documentation and examples, the word "module" is often used to refer to AWS Construct Library modules, one or more per AWS service, which differs from idiomatic Go usage of the term. The CDK Construct Library is provided in one Go module with the individual Construct Library modules, which support the various AWS services, provided as Go packages within that module.

Some services' AWS Construct Library support is in more than one Construct Library module (Go package). For example, Amazon Route 53 has three Construct Library modules in addition to the main `awsroute53` package, named `awsroute53patterns`, `awsroute53resolver`, and `awsroute53targets`.

The AWS CDK’s core package, which you’ll need in most AWS CDK apps, is imported in Go code as `github.com/aws/aws-cdk-go/awscdk/v2`. Packages for the various services in the AWS Construct Library live under `github.com/aws/aws-cdk-go/awscdk/v2`. For example, the Amazon S3 module’s namespace is `github.com/aws/aws-cdk-go/awscdk/v2/awss3`.

```
import (
        "github.com/aws/aws-cdk-go/awscdk/v2/awss3"
        // ...
)
```

Once you have imported the Construct Library modules (Go packages) for the services you want to use in your app, you access constructs in that module using, for example, `awss3.Bucket`.

## Managing dependencies in Go
<a name="work-with-cdk-go-dependencies"></a>

In Go, dependencies versions are defined in `go.mod`. The default `go.mod` is similar to the one shown here.

```
module my-package

go 1.16

require (
  github.com/aws/aws-cdk-go/awscdk/v2 v2.16.0
  github.com/aws/constructs-go/constructs/v10 v10.0.5
  github.com/aws/jsii-runtime-go v1.29.0
)
```

Package names (modules, in Go parlance) are specified by URL with the required version number appended. Go's module system does not support version ranges.

Issue the `go get` command to install all required modules and update `go.mod`. To see a list of available updates for your dependencies, issue `go list -m -u all`.

## AWS CDK idioms in Go
<a name="go-cdk-idioms"></a>

### Field and method names
<a name="go-naming"></a>

Field and method names use camel casing (`likeThis`) in TypeScript, the CDK’s language of origin. In Go, these follow Go conventions, so are Pascal-cased (`LikeThis`).

### Cleaning up
<a name="go-cdk-jsii-close"></a>

In your `main` method, use `defer jsii.Close()` to make sure your CDK app cleans up after itself.

### Missing values and pointer conversion
<a name="go-missing-values"></a>

In Go, missing values in AWS CDK objects such as property bundles are represented by `nil`. Go doesn’t have nullable types; the only type that can contain `nil` is a pointer. To allow values to be optional, then, all CDK properties, arguments, and return values are pointers, even for primitive types. This applies to required values as well as optional ones, so if a required value later becomes optional, no breaking change in type is needed.

When passing literal values or expressions, use the following helper functions to create pointers to the values.
+  `jsii.String`
+  `jsii.Number`
+  `jsii.Bool`
+  `jsii.Time`

For consistency, we recommend that you use pointers similarly when defining your own constructs, even though it may seem more convenient to, for example, receive your construct’s `id` as a string rather than a pointer to a string.

When dealing with optional AWS CDK values, including primitive values as well as complex types, you should explicitly test pointers to make sure they are not `nil` before doing anything with them. Go does not have "syntactic sugar" to help handle empty or missing values as some other languages do. However, required values in property bundles and similar structures are guaranteed to exist (construction fails otherwise), so these values need not be `nil`-checked.

### Constructs and Props
<a name="go-props"></a>

Constructs, which represent one or more AWS resources and their associated attributes, are represented in Go as interfaces. For example, `awss3.Bucket` is an interface. Every construct has a factory function, such as `awss3.NewBucket`, to return a struct that implements the corresponding interface.

All factory functions take three arguments: the `scope` in which the construct is being defined (its parent in the construct tree), an `id`, and `props`, a bundle of key/value pairs that the construct uses to configure the resources it creates. The "bundle of attributes" pattern is also used elsewhere in the AWS CDK.

In Go, props are represented by a specific struct type for each construct. For example, an `awss3.Bucket` takes a props argument of type `awss3.BucketProps`. Use a struct literal to write props arguments.

```
var bucket = awss3.NewBucket(stack, jsii.String("amzn-s3-demo-bucket"), &awss3.BucketProps{
    Versioned: jsii.Bool(true),
})
```

### Generic structures
<a name="go-generic-structures"></a>

In some places, the AWS CDK uses JavaScript arrays or untyped objects as input to a method. (See, for example, AWS CodeBuild’s [`BuildSpec.fromObject()`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_codebuild.BuildSpec.html#static-fromwbrobjectvalue) method.) In Go, these objects are represented as slices and an empty interface, respectively.

The CDK provides variadic helper functions such as `jsii.Strings` for building slices containing primitive types.

```
jsii.Strings("One", "Two", "Three")
```

### Working with any slice
<a name="go-any-slice"></a>

Certain constructs expect properties that are a list of multiple types (union types in TypeScript). In Go, these are as a slice of any (`*[]any`). The `any` ensures that the compiler will allow the assignment of different types there. Refer to the documentation for the ` [AWS CDK Go package](https://pkg.go.dev/github.com/aws/aws-cdk-go/awscdk/v2) ` to find out what the allowed types are.

To work with such properties, use the helper functions provided by `jsii` to create slices of any from different types:
+  `jsii.AnySlice`
+  `jsii.AnyStrings`
+  `jsii.AnyNumbers`

For example:

```
func Arns() *[]*string {
a := "arn:aws:s3:::bucket1"
b := "arn:aws:s3:::bucket2"
return &[]*string{&a, &b}
}

awsiam.NewCfnUser(stack, jsii.String("User"), &awsiam.CfnUserProps{
	ManagedPolicyArns: jsii.AnySlice(Arns())
  // or
	ManagedPolicyArns: jsii.AnyStrings("arn:aws:s3:::bucket1", "arn:aws:s3:::bucket2")
  // or
  ManagedPolicyArns: &[]interface{}{
    jsii.String("arn:aws:s3:::bucket1"),
    jsii.String("arn:aws:s3:::bucket2"),
  }
})
```

This approach ensures that your slices are correctly interpreted by the CDK, avoiding deserialization errors when deploying or synthesizing your stacks.

### Developing custom constructs
<a name="go-writing-constructs"></a>

In Go, it is usually more straightforward to write a new construct than to extend an existing one. First, define a new struct type, anonymously embedding one or more existing types if extension-like semantics are desired. Write methods for any new functionality you’re adding and the fields necessary to hold the data they need. Define a props interface if your construct needs one. Finally, write a factory function `NewMyConstruct()` to return an instance of your construct.

If you are simply changing some default values on an existing construct or adding a simple behavior at instantiation, you don’t need all that plumbing. Instead, write a factory function that calls the factory function of the construct you’re "extending." In other CDK languages, for example, you might create a `TypedBucket` construct that enforces the type of objects in an Amazon S3 bucket by overriding the `s3.Bucket` type and, in your new type’s initializer, adding a bucket policy that allows only specified filename extensions to be added to the bucket. In Go, it is easier to simply write a `NewTypedBucket` that returns an `s3.Bucket` (instantiated using `s3.NewBucket`) to which you have added an appropriate bucket policy. No new construct type is necessary because the functionality is already available in the standard bucket construct; the new "construct" just provides a simpler way to configure it.

## Building, synthesizing, and deploying
<a name="go-running"></a>

The AWS CDK automatically compiles your app before running it. However, it can be useful to build your app manually to check for errors and to run tests. You can do this by issuing `go build` at a command prompt while in your project’s root directory.

Run any tests you’ve written by running `go test` at a command prompt.

## Troubleshooting
<a name="go-troubleshooting"></a>

If you encounter a compiler error like the following, it means that string slices were passed directly to a property expecting a slice of any.

```
Cannot use 'jsii.Strings("arn:aws:s3:::bucket1", "arn:aws:s3:::bucket2")' (type *[]*string) as the type *[]interface{}
```

To resolve this error, replace `jsii.Strings()` with `jsii.AnyStrings()`. See this ` [CDK GitHub issue](https://github.com/aws/aws-cdk/issues/35630) ` for more context and additional solutions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
