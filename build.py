import os
import PyInstaller.__main__


def main():
    command = []

    # file to build
    command.append('--onefile')
    command.append('--windowed')
    command.append('--name=wingspan-stats')
    command.append('wingspan-stats.spec')

    PyInstaller.__main__.run(command)


if __name__ == '__main__':
    main()

print(os.name)
