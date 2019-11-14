# -*- coding: utf-8 -*-
# -*- author: ph -*-
import sys
import platform


class InfoCollection(object):
    """three different functions in python, they are getattr()、setattr()、hasattr()"""

    def collect(self):
        """
        collect platform info
        firstly, jugde what the platform now, exec different functions due to different platform
        """
        try:
            func = getattr(self, platform.system().lower())
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            sys.exit("不支持当前操作系统：[%s]!" % platform.system())

        @staticmethod
        def linux():
            from plugins.collect_linux_info import collect
            return collect

        @staticmethod
        def windows():
            from plugis.collect_windows_info import Win32Info
            return Win32Info().collect()

        @staticmethod
        def build_report_data(data):
            pass
            return data

"""python的platform模块"""
# python中，platform模块给我们提供了很多方法去获取操作系统的信息
#    如：
#        import platform
#        platfrom.system()          #获取操作系统  'Darwin'
#        platform.platform()   		#获取操作系统名称及版本号，'Darwin-18.6.0-x86_64-i386-64bit'
#        platform.version()      		#获取操作系统版本号，'Darwin Kernel Version 18.6.0: Thu Apr 25 23:16:27 PDT 2019; root:xnu-4903.261.4~2/RELEASE_X86_64'
#        platform.architecture()   	#获取操作系统的位数，('64bit', '')
#        platform.machine()   		#计算机类型，'x86_64'
#        platform.node()       			#计算机的网络名称，'diyidandeMacBook-Pro.local'
#        platform.processor()  		#计算机处理器信息，'i386'
#        platform.uname()      		#包含上面所有的信息汇总，uname_result(system='Darwin', node='diyidandeMacBook-Pro.local', release='18.6.0',
#                                                       version='Darwin Kernel Version 18.6.0: Thu Apr 25 23:16:27 PDT 2019;
#                                                       root:xnu-4903.261.4~2/RELEASE_X86_64', machine='x86_64', processor='i386')
#
#        还可以获得计算机中python的一些信息：
#        import platform
#        platform.python_build()
#        platform.python_compiler()
#        platform.python_branch()
#        platform.python_implementation()
#        platform.python_revision()
#        platform.python_version()
#        platform.python_version_tuple()

