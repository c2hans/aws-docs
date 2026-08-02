---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/typescript-best-practices.html
---

# Follow TypeScript best practices
<a name="typescript-best-practices"></a>

TypeScript is a language that extends the capabilities of JavaScript. It's a strongly typed and object-oriented language. You can use TypeScript to specify the types of data being passed within your code and has the ability to report errors when the types don't match. This section provides an overview of TypeScript best practices.

## Describe your data
<a name="describe-your-data.b9caab51-9f1d-5552-970c-7778b47b6a87"></a>

You can use TypeScript to describe the shape of objects and functions in your code. Using the `any` type is equivalent to opting out of type checking for a variable. We recommend that you avoid using `any` in your code. Here is an example.

```
type Result = "success" | "failure"
function verifyResult(result: Result) {
    if (result === "success") {
        console.log("Passed");
    } else {
        console.log("Failed")
    }
}
```

## Use enums
<a name="use-enums.84994a28-5629-562e-b872-7840de2b2590"></a>

You can use enums to define a set of named constants and define standards that can be reused in your code base. We recommend that you export your enums one time at the global level, and then let other classes import and use the enums. Assume that you want to create a set of possible actions to capture the events in your code base. TypeScript provides both numeric and string-based enums. The following example uses an enum.

```
enum EventType {
    Create,
    Delete,
    Update
}

class InfraEvent {
    constructor(event: EventType) {
        if (event === EventType.Create) {
            // Call for other function
            console.log(`Event Captured :${event}`);
        }
    }
}

let eventSource: EventType = EventType.Create;
const eventExample = new InfraEvent(eventSource)
```

## Use interfaces
<a name="use-interfaces.53fbe466-9ffe-5a3a-a3b1-236d24cbcd38"></a>

An interface is a contract for the class. If you create a contract, then your users must comply with the contract. In the following example, an interface is used to standardize the `props` and ensure that callers provide the expected parameter when using this class.

```
import { Stack, App } from "aws-cdk-lib";
import { Construct } from "constructs";

interface BucketProps {
    name: string;
    region: string;
    encryption: boolean;

}

class S3Bucket extends Stack {
    constructor(scope: Construct, props: BucketProps) {
        super(scope);
        console.log(props.name);

    }
}
const app = App();
const myS3Bucket = new S3Bucket(app, {
    name: "DOC-EXAMPLE-BUCKET",
    region: "us-east-1",
    encryption: false
})
```

Some properties can only be modified when an object is first created. You can specify this by putting `readonly` before the name of the property, as the following example shows.

```
interface Position {
    readonly latitude: number;
    readonly longitute: number;
}
```

## Extend interfaces
<a name="extend-interfaces.8f311a71-bbfd-5aba-ab58-7699ceafeb6f"></a>

Extending interfaces reduces duplication, because you don't have to copy the properties between interfaces. Also, the reader of your code can easily understand the relationships in your application.

```
 interface BaseInterface{
    name: string;
  }
  interface EncryptedVolume extends BaseInterface{
      keyName: string;
  }
  interface UnencryptedVolume extends BaseInterface {
      tags: string[];
  }
```

## Avoid empty interfaces
<a name="avoid-empty-interfaces.232c7129-8105-5850-82f0-1f4bc8ae37c7"></a>

We recommend that you avoid empty interfaces due to the potential risks they create. In the following example, there's an empty interface called `BucketProps`. The `myS3Bucket1` and `myS3Bucket2` objects are both valid, but they follow different standards because the interface doesn't enforce any contracts. This following code will compile and print the properties but this introduces inconsistency in your application.

```
interface BucketProps {}

class S3Bucket implements BucketProps {
    constructor(props: BucketProps){
        console.log(props);
    }
}

const myS3Bucket1 = new S3Bucket({
    name: "DOC-EXAMPLE-BUCKET",
    region: "us-east-1",
    encryption: false,
});

const myS3Bucket2 = new S3Bucket({
    name: "DOC-EXAMPLE-BUCKET",
});
```

## Use factories
<a name="use-factories.02641b2b-e130-54a7-ad28-b91842dde5e7"></a>

In an Abstract Factory pattern, an interface is responsible for creating a factory of related objects without explicitly specifying their classes. For example, you can create a Lambda factory for creating Lambda functions. Instead of creating a new Lambda function within your construct, you're delegating the creation process to the factory. For more information on this design pattern, see [Abstract Factory in TypeScript](https://refactoring.guru/design-patterns/abstract-factory/typescript/example) in the Refactoring.Guru documentation.

## Use destructuring on properties
<a name="use-destructuring-on-properties.79a91039-e6ed-536e-ab83-f443e1d16539"></a>

Destructuring, introduced in ECMAScript 6 (ES6), is a JavaScript feature that gives you the ability to extract multiple pieces of data from an array or object and assign them to their own variables.

```
const object = {
    objname: "obj",
    scope: "this",
};

const oName = object.objname;
const oScop = object.scope;

const { objname, scope } = object;
```

## Define standard naming conventions
<a name="naming-conventions"></a>

Enforcing a naming convention keeps the code base consistent and reduces overhead when thinking about how to name a variable. We recommend the following:
+ Use camelCase for variable and function names.
+ Use UPPER\_CASE for global constants to clearly indicate immutable compile-time values.
+ Use PascalCase for class names and interface names.
+ Use camelCase for interface members.
+ Use PascalCase for type names and enum names.
+ Name files with camelCase (for example, `ebsVolumes.tsx` or `storage.ts`)

The following shows examples of these recommended naming conventions:

```
// Variables and functions
const userName = 'john';
function getUserData() { }

// Global constants
const MAX_RETRY_ATTEMPTS = 3;
const API_BASE_URL = 'https://api.example.com';

// Classes and interfaces
class DatabaseConnection { }
interface UserProfile { }

// Types and enums
type ResponseStatus = 'success' | 'error';
enum HttpStatusCode { }
```

## Don't use the var keyword
<a name="don-t-use-the-var-keyword.2aac350c-4f5f-54c0-a71e-ba1df6dc2806"></a>

The `let` statement is used to declare a local variable in TypeScript. It's similar to the `var` keyword, but it has some restrictions in scoping compared to the `var` keyword. A variable declared in a block with `let` is only available for use within that block. The `var` keyword cannot be block-scoped, which means it can be accessed outside a particular block (represented by `{}`) but not outside of the function it's defined in. You can redeclare and update `var` variables. It's a best practice to avoid using the `var` keyword.

## Consider using ESLint and Prettier
<a name="consider-using-eslint-and-prettier.de3fa77b-3d52-56b7-89bb-478bc5404ef7"></a>

ESLint statically analyzes your code to quickly find issues. You can use ESLint to create a series of assertions (called *lint rules*) that define how your code should look or behave. ESLint also has auto-fixer suggestions to help you improve your code. Finally, you can use ESLint to load in lint rules from shared plugins.

Prettier is a well-known code formatter that supports a variety of different programming languages. You can use Prettier to set your code style so that you can avoid manually formatting your code. After installation, you can update your `package.json` file and run the `npm run format` and `npm run lint` commands.

The following example shows you how to enable ESLint and the Prettier formatter for your AWS CDK project.

```
"scripts": {
    "build": "tsc",
    "watch": "tsc -w",
    "test": "jest",
    "cdk": "cdk",
    "lint": "eslint --ext .js,.ts .",
    "format": "prettier --ignore-path .gitignore --write '**/*.+(js|ts|json)'"
}
```

## Use access modifiers
<a name="use-access-modifiers.56aee8f9-9748-527c-9899-4f4287dbdadf"></a>

The private modifier in TypeScript limits visibility to the same class only. When you add the private modifier to a property or method, you can access that property or method within the same class.

The public modifier allows class properties and methods to be accessible from all locations. If you don't specify any access modifiers for properties and methods, they will take the public modifier by default.

The protected modifier allows properties and methods of a class to be accessible within the same class and within subclasses. Use the protected modifier when you expect to create subclasses in your AWS CDK application.

## Use utility types
<a name="utility-types"></a>

*Utility types* in TypeScript are predefined type functions that perform transformations and operations on existing types. This helps you create new types based on existing types. For example, you can change or extract properties, make properties optional or required, or create immutable versions of types. By using utility types, you can define more precise types and catch potential errors at compile time.

### Partial<Type>
<a name="partial9999999999999999lt-type9999999999999999gt-.05adc9a6-2f79-57ef-b33d-8aa72f0fc3f3"></a>

`Partial` marks all members of an input type `Type` as optional. This utility returns a type that represents all subsets of a given type. The following is an example of `Partial`.

```
interface Dog {
  name: string;
  age: number;
  breed: string;
  weight: number;
}

let partialDog: Partial<Dog> = {};
```

### Required<Type>
<a name="required9999999999999999lt-type9999999999999999gt-.7464cc4d-1ce4-5dcc-8b00-7f4c4c43d7ae"></a>

`Required` does the opposite of `Partial`. It makes all members of an input type `Type` non-optional (in other words, required). The following is an example of `Required`.

```
interface Dog {
  name: string;
  age: number;
  breed: string;
  weight?: number;
}

let dog: Required<Dog> = {
  name: "scruffy",
  age: 5,
  breed: "labrador",
  weight: 55 // "Required" forces weight to be defined
};
```
