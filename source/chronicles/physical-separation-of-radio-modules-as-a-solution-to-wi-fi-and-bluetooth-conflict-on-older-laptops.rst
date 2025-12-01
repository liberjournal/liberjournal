###################################################################################################
Physical Separation of Radio Modules as a Solution to Wi-Fi and Bluetooth Conflict on Older Laptops
###################################################################################################

:Author: Nur Y.
:Date: 01 December 2025

Environment
***********

=========================  ===================================================
Architecture               x86_64
Host OS                    RHEL 9.7 Workstation
Network Controller         Qualcomm Atheros QCA9565 / AR9565 Wireless Adapter
Frequency                  2.4 GHz
=========================  ===================================================

On a 2014 laptop equipped with a Qualcomm Atheros QCA9565 / AR9565 Wireless Adapter combo module, simultaneous Wi-Fi and Bluetooth operation is unstable. Both standards utilise the 2.4 GHz band, forcing the single radio module to switch between them via Time Division Multiplexing (TDM). Due to high packet density, streaming Bluetooth audio practically monopolises the channel.

As the hardware does not support 5 GHz and a wired internet connection sacrifices mobility and convenience, I resolved the issue by physically separating the controllers. I retained the built-in chip solely for Bluetooth and connected an external Realtek RTL8188EUS (802.11n) USB adapter for Wi-Fi. Although signal interference in the air persists, this eliminated the primary issue: competition for the single radio module's active time.

Instead of disabling the built-in Wi-Fi via software—which risked cutting power to the Bluetooth module as well—I simply deleted the saved networks from it and configured the connection via the USB adapter. Separating the interfaces completely resolved the resource conflict; Bluetooth now operates stably, and Wi-Fi maintains high speeds.