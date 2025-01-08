# Linux Vivado Installtion
Vivado Installtion process

1. Open terminal and type these commands
```bash
sudo apt update & sudo apt upgrade
sudo apt install build-essential
sudo apt-get install libstdc++6:i386
sudo apt-get install libgtk2.0-0:i386
sudo apt-get install dpkg-dev:i386
sudo apt install python3-pip
sudo apt install libtinfo6 libncurses6
```

2. Download Vivado HLx 2020.2: All OS installer Single-File Download (TAR/GZIP - 43.07 GB)


click on this link [Vivado 2020.2](https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/vivado-design-tools/archive.html)


```{figure} ./images/img1.png
:align: center
```
After clicking for download, you will be prompted to log in. If you don't have an account, please create one to proceed. If you already have an account, simply log in

3. After downloading go the folder where you have downloaded the tar.gz file.Open terminal on same location and run these commands.

```bash
# change file name if it is different name
tar -xvf Xilinx_Unified_2020.2_1118_1232.tar.gz
cd Xilinx_Unified_2020.2_1118_1232/
chmod +x xsetup
sudo ./xsetup
```
4. Start Screen Visible
```{figure} ./images/img2.png
:align: center
```
5. Click next

```{figure} ./images/img3.png
:align: center
```
6. Select vitis and click next

```{figure} ./images/img4.png
:align: center
```
7. Check checkboxes according to this image and click next.

```{figure} ./images/img5.png
:align: center
```
8. Check checkboxes and click next
```{figure} ./images/img6.png
:align: center
```
9. Change the loaction if needed. Default location is  /tool/Xilinx.(Recommendation change the loaction to /home/Xilinx)
```{figure} ./images/img7.png
:align: center
```
10. Click next and wait for Installtion.
```{figure} ./images/img8.png
:align: center
```

11. After installtion run these commands on terminal and change location according to your location

```bash
sudo ./tools/Xilinx/Vivado/2020.2/data/xicom/cable_drivers/lin64/install_script/install_drivers/install_drivers
#if the above  command does not have executable permission then run the below  command first and then run the above again
chmod +x /tools/Xilinx/Vivado/2020.2/data/xicom/cable_drivers/lin64/install_script/install_drivers/install_drivers
```
```bash
sudo ./tools/Xilinx/Vitis/2020.2/scripts/installLibs.sh
#if the above  command does not have executable permission then run the below  command first and then run the above again
chmod +x /tools/Xilinx/Vitis/2020.2/scripts/installLibs.sh
```
13. Run these commands on terminal. Change location according to your path

```bash
echo 'export PATH="$PATH:/tools/Xilinx/Vitis/2020.2/bin"' >> ~/.bashrc
echo 'export PATH="$PATH:/tools/Xilinx/Vivado/2020.2/bin"' >> ~/.bashrc
echo 'export PATH="$PATH:/tools/Xilinx/Vitis_HLS/2020.2/bin"' >> ~/.bashrc
source ~/.bashrc
echo $PATH
```
14. Open new terminal and type vivado in terminal
```{figure} ./images/img9.png
:align: center
```
15. Download Board file using click on this link :- [Pynq-z2](https://github.com/ankur-gupta-29/EE705-VLSI-DESIGN-LAB/raw/baa2e938296cb95ad102f738f160ecfa36a92ae5/source/board_files/pynq-z2.zip)
. Unzip the .zip file and copy that folder (named pynq-z2) to Location :  /tools/Xilinx/Vivado/2020.2/data/boards/board_files/


