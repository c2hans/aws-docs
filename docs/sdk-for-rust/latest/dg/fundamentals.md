---
source_url: https://docs.aws.amazon.com/sdk-for-rust/latest/dg/fundamentals.html
---

# Fundamentals for the AWS SDK for Rust
<a name="fundamentals"></a>

Learn fundamentals for programming with the AWS SDK for Rust, such as: Rust programming language fundamentals, information about SDK for Rust crates, project configuration, and SDK for Rust's use of the Tokio runtime.

## Prerequisites
<a name="prerequisites"></a>

In order to use the AWS SDK for Rust, you must have Rust and Cargo installed.
+ Install the Rust toolchain: [https://www.rust-lang.org/tools/install](https://www.rust-lang.org/tools/install)
+ Install the `cargo-component` [tool](https://github.com/bytecodealliance/cargo-component) by running command: `cargo install cargo-component`

### Recommended tools:
<a name="recommended-tools"></a>

The following optional tools can be installed in your IDE to assist with code completion and troubleshooting.
+ The rust-analyzer extension, see [Rust in Visual Studio Code](https://code.visualstudio.com/docs/languages/rust).
+ Amazon Q Developer, see [Installing the Amazon Q Developer extension or plugin in your IDE](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-IDE-setup.html).

## Rust fundamentals
<a name="rust-fundamentals"></a>

The following are some basics of the Rust programming language that would be helpful to know. All references for more information come from [The Rust Programming Language](https://doc.rust-lang.org/book/title-page.html#the-rust-programming-language).
+ `Cargo.toml` is the standard Rust project configuration file, it contains the dependencies and some metadata about the project. Rust source files have a `.rs` file extension. See [Hello, Cargo\!](https://doc.rust-lang.org/book/ch01-03-hello-cargo.html).
  + The `Cargo.toml` can be customized with profiles, see [Customizing Builds with Release Profiles](https://doc.rust-lang.org/book/ch14-01-release-profiles.html). These profiles are completely unrelated and independent from AWS's use of profiles within the shared AWS `config` file.
  + A common way to add library dependencies to your project and this file is to use `cargo add`. See [`cargo-add`](https://doc.rust-lang.org/cargo/commands/cargo-add.html).
+ Rust has a basic function structure like the following. The `let` keyword declares a variable and might be paired with assignment (=). If you don't specify a type after `let`, then the compiler will infer one. See [Variables and Mutability](https://doc.rust-lang.org/book/ch03-01-variables-and-mutability.html).

  ```
  fn main() {
      let w = "world";
      println!("Hello {}!", w);
  }
  ```
+ To declare a variable `x` with an explicit type `T`, Rust uses syntax `x: T`. See [Data Types](https://doc.rust-lang.org/book/ch03-02-data-types.html).
+ `struct X {}` defines the new type `X`. Methods are implemented on the custom struct type `X`. Methods for type `X` are declared with implementation blocks prefixed with keyword `impl`. Inside the implementation block, `self` refers to the instance of the struct that the method was called on. See [Keyword `impl`](https://doc.rust-lang.org/std/keyword.impl.html) and [Method Syntax](https://doc.rust-lang.org/book/ch05-03-method-syntax.html).
+ If an exclamation point ("\!") follows what appears to be a function definition or function call, then the code is defining or calling a macro. See [Macros](https://doc.rust-lang.org/book/ch19-06-macros.html?highlight=macro#macros).
+ In Rust, unrecoverable errors are represented by the `panic!` macro. When a program encounters a `panic!` it will stop running, print a failure message, unwind, clean up the stack, and quit. See [Unrecoverable Errors with `panic!`](https://doc.rust-lang.org/book/ch09-01-unrecoverable-errors-with-panic.html).
+ Rust doesn't support inheritance of functionality from base classes like other programming languages do; `traits` are how Rust provides the overloading of methods. Traits might be thought of as being conceptually similar to an interface. However, traits and true interfaces have differences and are often used differently in the design process. See [Traits: Defining Shared Behavior](https://doc.rust-lang.org/book/ch10-02-traits.html).
  + Polymorphism refers to code that supports functionality for multiple data types without having to individually write each one. Rust supports polymorphism through enums, traits, and generics. See [Inheritance as a Type System and as Code Sharing](https://doc.rust-lang.org/book/ch17-01-what-is-oo.html?#inheritance-as-a-type-system-and-as-code-sharing).
+ Rust is very explicit about memory. Smart pointers "are data structures that act like a pointer but also have additional metadata and capabilities". See [Smart Pointers](https://doc.rust-lang.org/book/ch15-00-smart-pointers.html).
  + The type `Cow` is a clone-on-write smart pointer that helps transfer memory ownership to the caller when necessary. See [`Enum std::borrow::Cow`](https://doc.rust-lang.org/std/borrow/enum.Cow.html).
  + The type `Arc` is a Atomically Reference Counted smart pointer that counts allocated instances. See [`Struct std::sync::Arc`](https://doc.rust-lang.org/std/sync/struct.Arc.html).
+ The SDK for Rust frequently uses the builder pattern for constructing complex types.

## AWS SDK for Rust crate fundamentals
<a name="aws-sdk-crate-fundamentals"></a>
+ The primary core crate for the SDK for Rust functionality is `aws-config`. This is included in the majority of projects because it provides functionality to read configuration from the environment.

  ```
  $ cargo add aws-config
  ```
  + Don't confuse this with the AWS service that is called AWS Config. Since that is a service, it follows the standard convention of AWS service crates and is called `aws-sdk-config`.
+ The SDK for Rust library is separated into different library crates by each AWS service. These crates are available at [https://docs.rs/](https://docs.rs/).
+ AWS service crates follow the naming convention of `aws-sdk-{{[servicename]}}`, such as `aws-sdk-s3` and `aws-sdk-dynamodb`.

## Project configuration for working with AWS services
<a name="project-configuration-for-working-with-aws-services"></a>
+ You will need to add a crate to your project for each AWS service that you want your application to use.
+ The recommended way to add a crate is using the command line in your project's directory by running `cargo add {{[crateName]}}`, such as `cargo add aws-sdk-s3`.
  + This will add a line to your project's `Cargo.toml` under `[dependencies]`.
  + By default, this will add the latest version of the crate to your project.
+ In your source file, use the `use` statement to bring items from their crates into scope. See [Using External Packages](https://doc.rust-lang.org/book/ch07-04-bringing-paths-into-scope-with-the-use-keyword.html#using-external-packages) on the Rust Programming Language website.
  + Crate names are often hyphenated, but the hyphens get converted to underscores when actually using the crate. For example, the `aws-config` crate is used in code `use` statement as: `use aws_config`.
+ Configuration is a complex topic. Configuration can occur directly in code, or be specified externally in environment variables or config files. For more information, see [Configuring AWS SDK for Rust service clients externally](config-external.md).
  + When the SDK loads your configuration, invalid values are logged instead of halting execution because most settings have reasonable defaults. To learn how to turn on logging, see [Configuring and using logging in the AWS SDK for Rust](logging.md).
  + Most environment variables and config file settings are loaded once when your program starts. Any updates to the values will not be seen until you restart your program.

## Tokio runtime
<a name="tokio-runtime"></a>
+ Tokio is an asynchronous runtime for the SDK for Rust programming language, it executes the `async` tasks. See [tokio.rs](http://tokio.rs/) and [docs.rs/tokio](http://docs.rs/tokio).
+ The SDK for Rust requires an async runtime. We recommend you add the following crate to your projects:

  ```
  $ cargo add tokio --features=full
  ```
+ The `tokio::main` attribute macro creates an async main entry point to your program. To use this macro, add it to the line before your `main` method, as shown in the following:

  ```
  #[tokio::main]
  async fn main() -> Result<(), Error> {
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for Rust. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-rust` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
