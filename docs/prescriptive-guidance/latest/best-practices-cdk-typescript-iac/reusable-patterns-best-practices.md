---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/best-practices-cdk-typescript-iac/reusable-patterns-best-practices.html
---

# Develop reusable patterns
<a name="reusable-patterns-best-practices"></a>

Software design patterns are reusable solutions to common problems in software development. They act as a guide or paradigm to help software engineers create products that follow best practices. This section provides an overview of two reusable patterns that you can use in your AWS CDK codebase: the Abstract Factory pattern and the Chain of Responsibility pattern. You can use each pattern as a blueprint and customize it for the particular design problem in your code. For more information on design patterns, see [Design Patterns](https://refactoring.guru/design-patterns) in the Refactoring.Guru documentation.

## Abstract Factory
<a name="abstract-factory.776a8889-7abe-5013-9cc0-1d2c268e464f"></a>

The Abstract Factory pattern provides interfaces for creating families of related or dependent objects without specifying their concrete classes. This pattern applies to the following use cases:
+ When the client is independent of how you create and compose the objects in the system
+ When the system consists of multiple families of objects, and these families are designed to be used together
+ When you must have a runtime value to construct a particular dependency

For more information about the Abstract Factory pattern, see [Abstract Factory in TypeScript](https://refactoring.guru/design-patterns/abstract-factory/typescript/example) in the Refactoring.Guru documentation.

The following code example shows how the Abstract Factory pattern can be used to build an Amazon Elastic Block Store (Amazon EBS) storage factory.

```
abstract class EBSStorage {
    abstract initialize(): void;
}

class ProductEbs extends EBSStorage{
    constructor(value: String) {
        super();
        console.log(value);
    }
    initialize(): void {}
}

abstract class AbstractFactory {
    abstract createEbs(): EBSStorage
}

class EbsFactory extends AbstractFactory {
    createEbs(): ProductEbs{
        return new ProductEbs('EBS Created.')
    }
}

const ebs = new EbsFactory();
ebs.createEbs();
```

## Chain of Responsibility
<a name="chain-of-responsibility.a2d1b771-e9d7-57c2-9282-7614c6999771"></a>

Chain of Responsibility is a behavioral design pattern that enables you to pass a request along the chain of potential handlers until one of them handles the request. The Chain of Responsibility pattern applies to the following use cases:
+ When multiple objects, determined at runtime, are candidates to handle a request
+ When you don't want to specify handlers explicitly in your code
+ When you want to issue a request to one of several objects without specifying the receiver explicitly

For more information about the Chain of Responsibility pattern, see [Chain of Responsibility in TypeScript](https://refactoring.guru/design-patterns/chain-of-responsibility/typescript/example) in the Refactoring.Guru documentation.

The following code shows an example of how the Chain of Responsibility pattern is used to build a series of actions that are required for completing the task.

```
interface Handler {
    setNext(handler: Handler): Handler;
    handle(request: string): string;
}
abstract class AbstractHandler implements Handler
{
    private nextHandler: Handler;
    public setNext(handler: Handler): Handler {
        this.nextHandler = handler;
        return handler;
    }

    public handle(request: string): string {
        if (this.nextHandler) {
            return this.nextHandler.handle(request);
        }
        return '';
    }
}

class KMSHandler extends AbstractHandler {
    public handle(request: string): string {
        return super.handle(request);
    }
}
```
