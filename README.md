<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">THIRD EYE</h1>
</p>
<p align="center">
    <em>Precision Port Scanning at Lightning Speed</em>
</p>
<p align="center">
    <img src="https://img.shields.io/github/license/abhishek-pokhrel/Third-Eye-PortScanner?style=flat&color=0080ff" alt="license">
    <img src="https://img.shields.io/github/last-commit/abhishek-pokhrel/Third-Eye-PortScanner?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
    <img src="https://img.shields.io/github/languages/top/abhishek-pokhrel/Third-Eye-PortScanner?style=flat&color=0080ff" alt="repo-top-language">
    <img src="https://img.shields.io/github/languages/count/abhishek-pokhrel/Third-Eye-PortScanner?style=flat&color=0080ff" alt="repo-language-count">
<p>
<p align="center">
        <em>Developed with the software and tools below.</em>
</p>
<p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>
<hr>

##  Quick Links

> - [ Overview](#overview)
> - [ Features](#-features)
> - [ Repository Structure](#-repository-structure)
> - [ Getting Started](#-getting-started)
>   - [ Installation](#-installation)
>   - [ Running Third-Eye-PortScanner](#-running-Third-Eye-PortScanner)
> - [ Contributing](#-contributing)
> - [ License](#-license)
> - [ Acknowledgments](#-acknowledgments)

---

##  Overview

THIRD EYE is a professional-grade port scanner designed to provide fast and reliable identification of open ports on a target system. Utilizing advanced multi-threading techniques, THIRD EYE ensures efficient and comprehensive scanning, making it an essential tool for network administrators and security professionals. `overview`

---

##  Features

Multi-threaded Scanning: By leveraging concurrent threads, THIRD EYE can scan multiple ports simultaneously, significantly reducing the time required to complete a scan.

Customizable Parameters: Users can define the range of ports to scan, the number of threads to use, and choose between verbose or concise output, providing flexibility to suit different needs and scenarios.

Color-coded Output: With the integration of the colorama library, THIRD EYE presents scan results in a clear and visually appealing manner, using colors to differentiate between open and closed ports.

Graceful Interrupt Handling: THIRD EYE is equipped to handle user interruptions gracefully, ensuring that the scan can be stopped at any time while still providing a summary of the results obtained so far.

Error Reporting: Comprehensive error handling and logging ensure that users are informed of any issues encountered during the scan, such as invalid hostnames or socket errors, enabling quick troubleshooting. `features`

---

##  Repository Structure

```sh
└── Third-Eye-PortScanner/
    ├── README.md
    ├── requirements.txt
    └── scanner.py
```

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.6`

###  Installation

1. Clone the Third-Eye-PortScanner repository:

```sh
git clone https://github.com/abhishek-pokhrel/Third-Eye-PortScanner
```

2. Change to the project directory:

```sh
cd Third-Eye-PortScanner
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```

###  Running Third-Eye-PortScanner

Use the following command to run Third-Eye-PortScanner:

```sh
python scanner.py HOST -sp StartPort -ep EndPort

python scanner.py 127.0.0.1 -sp 1 -ep 65535 -v
```

---

##  Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/abhishek-pokhrel/Third-Eye-PortScanner/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/abhishek-pokhrel/Third-Eye-PortScanner/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/abhishek-pokhrel/Third-Eye-PortScanner/issues)**: Submit bugs found or log feature requests for Third-eye-portscanner.

<details closed>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/abhishek-pokhrel/Third-Eye-PortScanner
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---

##  License

This project is protected under the MIT License. For more details, refer to the [LICENSE](https://github.com/abhishek-pokhrel/Third-Eye-PortScanner/blob/master/LICENSE) file.

---

##  Acknowledgments

- List any resources, contributors, inspiration, etc. here.

[**Return**](#-quick-links)

---
