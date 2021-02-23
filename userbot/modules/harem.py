from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^mash(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0)
    await typew.edit("/protecc shuten martha altera Atalante penthesilea quetzalcoatl jinako chevalier artoria qin rhyme mata")
    sleep(0)
    await typew.edit("/protecc shiki yi medb osakabehime kiyohime Nightingale yu ke Hokusai Carmilla Mysterious Mae drake europa")
    sleep(0)
    await typew.edit("/protecc boudica chacha circe medea murasaki kiara ishtar jeanne jane bradamante brynhildr tomoe gozen")
    sleep(0)
    await typew.edit("/protecc irisviel von katou medusa parvati orion stheno euryale nero kingprotea hassan yang abigail")
    sleep(0)
    await typew.edit("/protecc illyasviel ereshkigal bb charlotte tamamo chiyome minamoto wu helena ibaraki okita oda mash astolfo")
    sleep(0)
    await typew.edit("/protecc mordred nitocris gorgon paul benienma mecha elisabeth gray jack marie anastasia passionlip")
    sleep(0)
    await typew.edit("/protecc scheherazade semiramis salome lakshmibai valkyrie anne da fujino nagao")
    sleep(1)
    await typew.edit("udah")
    sleep(1)
    await typew.edit("udahhh")
# Owner @erruuu - @salama219


@register(outgoing=True, pattern='^xx(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0)
    await typew.edit("/protecc mysterious heroine x xx")
# Owner @erruuu - @salama219


@register(outgoing=True, pattern='^nana(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(0)
    await typew.edit("/protecc hikari oono kirigaya mio atago gaen araragi chisa yuuna izumi izuna nao ruka rikka erice erika chihiro nakano uesugi yui yukino hanyuu medusa mito mii boudica akari tomoe mami papi kagome beatrice eru kyons sister sae cabashira ichinose rias kanao akeno futaba koneko meteora aoko kyouko shinku youmu ryouko asuna haruhi natsumi lelei margaret")
# Owner @erruuu - @salama219


CMD_HELP.update({
    "harem":
    "`mash`\
\nUsage: Protecc servant (v.2).\
\n\n`nana`\
\nUsage: Protecc loli (v.1).\
\n\n`xx`\
\nUsage: Protecc servant char mysterious."
})
