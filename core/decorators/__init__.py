# Ultroid - UserBot
# Copyright (C) 2020-2023 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.


from contextlib import suppress

from database import udB

from ._wrappers import eod, eor

# ----------------------------------------------#
StatsHolder = {}

def should_allow_sudos():
    return udB.get_key("SUDO")


def get_sudos() -> list:
    return udB.get_key("SUDOS") or []  # type: ignore


def is_sudo(userid):
    return userid in get_sudos()


def owner_and_sudos(only_full=False):
    if only_full:
        return [udB.get_config("OWNER_ID"), *fullsudos()]
    return [udB.get_config("OWNER_ID"), *get_sudos()]


def _parse(key):
    with suppress(TypeError):
        return int(key)
    return key


def fullsudos():
    fullsudos = []
    if sudos := udB.get_key("FULLSUDO"):
        fullsudos.extend(str(sudos).split())
    owner = udB.get_config("OWNER_ID")
    if owner and owner not in fullsudos:
        fullsudos.append(owner)
    return list(map(_parse, filter(lambda id: id, fullsudos)))

# ------------------------------------------------ #