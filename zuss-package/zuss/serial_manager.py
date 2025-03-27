import serial


class SerialPort:
    def __init__(self, port, baudrate=115200, timeout=2, bytesize=8):
        """
        初始化串口
        :param port: 串口号，如'COM3'（Windows）或'/dev/ttyUSB0'（Linux）
        :param baudrate: 波特率
        :param timeout: 读取操作的超时时间（秒）
        """
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.bytesize = bytesize
        self._serial = None

    def open(self):
        """打开串口"""
        try:
            self._serial = serial.Serial(
                port=self.port,
                baudrate=self.baudrate,
                timeout=self.timeout,
                bytesize=self.bytesize,
                stopbits=serial.STOPBITS_ONE,
            )
        except Exception as e:
            print(f"打开串口 {self.port} 失败: {e}")

    def close(self):
        """关闭串口"""
        if self._serial is not None and self._serial.isOpen():
            self._serial.close()

    def write(self, data):
        """向串口写入数据
        :param data: 要写入的数据（字节串）
        """

        if self._serial is not None:
            if self._serial.isOpen():
                ret = self._serial.write(data)
                return ret

        return b""

    def readline(self):
        """从串口读取一行数据（以换行符结束）
        :return: 读取到的数据（字节串）
        """
        if self._serial is not None and self._serial.isOpen():
            return self._serial.readline().decode("Ascii")
        return b""

    def __enter__(self):
        """上下文管理器进入方法，打开串口"""
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """上下文管理器退出方法，关闭串口"""
        self.close()
