---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/build-cmake.html
---

# Creating a simple application using the AWS SDK for C\+\+
<a name="build-cmake"></a>

 [CMake](https://cmake.org/) is a build tool that you use to manage your application’s dependencies and to create makefiles suitable for the platform you’re building on. You can use CMake to create and build projects using the AWS SDK for C\+\+.

This example reports the Amazon S3 buckets you own. Having an Amazon S3 bucket in your AWS account is not required for this example, but it will be far more interesting if you have at least one. See [Create a Bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) in the *Amazon Simple Storage Service User Guide* if you don't already have one.

## Step 1: Write the code
<a name="setting-up-a-cmake-project"></a>

This example consists of one folder containing one source file (`hello_s3.cpp`) and one `CMakeLists.txt` file. The program uses Amazon S3 to report storage bucket information. This code is also available in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/s3/hello_s3) on GitHub.

You can set many options in a `CMakeLists.txt` build configuration file. For more information, see the [CMake tutorial](https://cmake.org/cmake-tutorial/) on the CMake website.

**Note**
Deep Dive: Setting `CMAKE_PREFIX_PATH`
By default, the AWS SDK for C\+\+ on macOS, Linux, Android and other non-Windows platforms is installed into `/usr/local` and on Windows is installed into `\Program Files (x86)\aws-cpp-sdk-all`.
When you install the AWS SDK to these standard locations, CMake automatically finds the necessary resources. However, if you install the AWS SDK to a custom location, you must tell CMake where to find the following resources that result from building the SDK:
`AWSSDKConfig.cmake`: A configuration file that tells CMake how to find and use the AWS SDK libraries in your project. Without this file, CMake cannot locate AWS SDK header files, link to AWS SDK libraries, or set up the proper compiler flags.
(for version 1.8 and earlier) The location of dependencies: `aws-c-event-stream`, `aws-c-common`, `aws-checksums`
To set a custom installation path:

```
cmake -DCMAKE_PREFIX_PATH=/path/to/your/aws-sdk-installation /path/to/project/you/are/building
```
If you don't set `CMAKE_PREFIX_PATH` for a custom installation, your build will fail with errors like "Could not find AWSSDK" when CMake tries to process `find_package(AWSSDK)` in your `CMakeLists.txt`.

**Note**
Deep Dive: Windows Runtime Libraries
To run your program, several DLLs are required in your program's executable location: `aws-c-common.dll`, `aws-c-event-stream.dll`, `aws-checksums.dll`, `aws-cpp-sdk-core.dll`, as well as any specific DLLs based on the components of your program (this example also requires `aws-cpp-sdk-s3` because it uses Amazon S3). The second `if` statement in the `CMakeLists.txt` file copies these libraries from the installation location to the executable location to satisfy this requirement. `AWSSDK_CPY_DYN_LIBS` is a macro defined by AWS SDK for C\+\+ that copies the SDK's DLLs from the installation location to the executable location of your program. If these DLLs are not in the executable location then runtime exceptions of 'file not found' occur. Review this portion of the `CMakeLists.txt` file for necessary changes for your unique environment if you encounter these errors.

**To create the folder and source files**

1. Create a `hello_s3` directory and/or project to hold your source files.
**Note**
To complete this example in Visual Studio: choose **Create New Project** and then choose **CMake Project**. Name the project `hello_s3`. This project name is used in the `CMakeLists.txt` file.

1. Within that folder, add a `hello_s3.cpp` file that includes the following code, which reports the Amazon S3 buckets you own.

   ```
   #include <aws/core/Aws.h>
   #include <aws/s3/S3Client.h>
   #include <iostream>
   #include <aws/core/auth/AWSCredentialsProviderChain.h>
   using namespace Aws;
   using namespace Aws::Auth;

   /*
    *  A "Hello S3" starter application which initializes an Amazon Simple Storage Service (Amazon S3) client
    *  and lists the Amazon S3 buckets in the selected region.
    *
    *  main function
    *
    *  Usage: 'hello_s3'
    *
    */

   int main(int argc, char **argv) {
       Aws::SDKOptions options;
       // Optionally change the log level for debugging.
   //   options.loggingOptions.logLevel = Utils::Logging::LogLevel::Debug;
       Aws::InitAPI(options); // Should only be called once.
       int result = 0;
       {
           Aws::Client::ClientConfiguration clientConfig;
           // Optional: Set to the AWS Region (overrides config file).
           // clientConfig.region = "us-east-1";

           // You don't normally have to test that you are authenticated. But the S3 service permits anonymous requests, thus the s3Client will return "success" and 0 buckets even if you are unauthenticated, which can be confusing to a new user.
           auto provider = Aws::MakeShared<DefaultAWSCredentialsProviderChain>("alloc-tag");
           auto creds = provider->GetAWSCredentials();
           if (creds.IsEmpty()) {
               std::cerr << "Failed authentication" << std::endl;
           }

           Aws::S3::S3Client s3Client(clientConfig);
           auto outcome = s3Client.ListBuckets();

           if (!outcome.IsSuccess()) {
               std::cerr << "Failed with error: " << outcome.GetError() << std::endl;
               result = 1;
           } else {
               std::cout << "Found " << outcome.GetResult().GetBuckets().size()
                         << " buckets\n";
               for (auto &bucket: outcome.GetResult().GetBuckets()) {
                   std::cout << bucket.GetName() << std::endl;
               }
           }
       }

       Aws::ShutdownAPI(options); // Should only be called once.
       return result;
   }
   ```

1. Add a `CMakeLists.txt` file that specifies your project’s name, executables, source files, and linked libraries.

   ```
   # Set the minimum required version of CMake for this project.
   cmake_minimum_required(VERSION 3.13)

   # Set the AWS service components used by this project.
   set(SERVICE_COMPONENTS s3)

   # Set this project's name.
   project("hello_s3")

   # Set the C++ standard to use to build this target.
   # At least C++ 11 is required for the AWS SDK for C++.
   set(CMAKE_CXX_STANDARD 11)

   # Use the MSVC variable to determine if this is a Windows build.
   set(WINDOWS_BUILD ${MSVC})

   if (WINDOWS_BUILD) # Set the location where CMake can find the installed libraries for the AWS SDK.
       string(REPLACE ";" "/aws-cpp-sdk-all;" SYSTEM_MODULE_PATH "${CMAKE_SYSTEM_PREFIX_PATH}/aws-cpp-sdk-all")
       list(APPEND CMAKE_PREFIX_PATH ${SYSTEM_MODULE_PATH})
   endif ()

   # Find the AWS SDK for C++ package.
   find_package(AWSSDK REQUIRED COMPONENTS ${SERVICE_COMPONENTS})

   if (WINDOWS_BUILD AND AWSSDK_INSTALL_AS_SHARED_LIBS)
       # Copy relevant AWS SDK for C++ libraries into the current binary directory for running and debugging.

       # set(BIN_SUB_DIR "/Debug") # if you are building from the command line you may need to uncomment this
       # and set the proper subdirectory to the executables' location.

       AWSSDK_CPY_DYN_LIBS(SERVICE_COMPONENTS "" ${CMAKE_CURRENT_BINARY_DIR}${BIN_SUB_DIR})
   endif ()

   add_executable(${PROJECT_NAME}
           hello_s3.cpp)

   target_link_libraries(${PROJECT_NAME}
           ${AWSSDK_LINK_LIBRARIES})
   ```

## Step 2: Build with CMake
<a name="building-with-cmake"></a>

CMake uses the information in `CMakeLists.txt` to build an executable program.

We recommend building the application following standard practices for your IDE.

**To build the application from the command line**

1. Create a directory where ** `cmake` ** will build your application.

   ```
   mkdir my_project_build
   ```

1. Change to the build directory and run ** `cmake` ** using the path to your project’s source directory.

   ```
   cd my_project_build
   cmake ../
   ```

1. After ** `cmake` ** generates your build directory, you can use ** `make` ** (or ** `nmake` ** on Windows), or MSBUILD (`msbuild ALL_BUILD.vcxproj` or `cmake --build . --config={{Debug}}`) to build your application.

## Step 3: Run
<a name="run-app"></a>

When you run this application, it displays console output that lists the total number of Amazon S3 buckets and the name of each bucket.

We recommend running the application following standard practices for your IDE.

**Note**
Remember to sign in\! If you are using IAM Identity Center to authenticate, remember to sign in using the AWS CLI `aws sso login` command.

**To run the program via command line**

1. Change to the Debug directory where the result of the build was generated.

1. Run the program using the name of the executable.

   ```
   hello_s3
   ```

For additional examples using the AWS SDK for C\+\+, see [Guided examples for calling AWS services using the AWS SDK for C\+\+](programming-services.md).
