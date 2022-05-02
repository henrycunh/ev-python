<div align="center">

# ev-python
  <strong>The official 🐍 Python package for <a href="https://github.com/henrycunh/ev">ev</a></strong><br/>
  <sup>a tool for versioning, securing and easily sharing environment variables</sup>

</div>


<p align="center">
  <table>
    <tbody>
      <td align="center">
        <img width="2000" height="0"><br>
        <a href="#initializing">initializing</a> • <a href="#commands">commands</a> • <a href="#using-in-your-project">using in your project</a><br>
        <img width="2000" height="0">
      </td>
    </tbody>
  </table>
</p>

## Features
- ⏱ **Version control** - allows for storing environment variables securely in git
- 🔑 **Secure** - uses a single secret to secure your variables
- 🧑‍💻 **Easy sharing** - sharing the secret means sharing your variables
- 🛠 **Great DX** - tools for easily managing variables  

## Getting started
This package exposes a *read-only* function for reading `ev` compatible variable files.

To manage and secure your environment variables, you must use the official CLI.

**[Read to `ev` documentation →]()**

## Usage
```bash
poetry add evpython
```
<sup>↳ Installs the dependency on your project</sup>


```python
# app.py
from evpython import load_environment
load_environment()
```
<sup>↳ Loads the default environment variables using either a `secret` file, or the `EV_SECRET` environment variable.</sup>


```python
# app.py
from evpython import load_environment
load_environment(secret='my-secret')
```
<sup>↳ Loads the default environment variables using the `my-secret` as the secret.</sup>


```python
# app.py
from evpython import load_environment
load_environment('production')
```
<sup>↳ Loads the `production` environment variables using either a `secret` file, or the `EV_SECRET` environment variable.</sup>


