/**
 * @file    myLKM.c
 * @author  Moisés Noguera Carrillo
 * @date    11 April 2022
 * @version 0.1
 * @brief  Un ejemplo simple de LKM que muestra un mensaje en los logs del kernel
 * cuando es iniciado y otro cuando se deja de usar.
*/

#include <linux/init.h>             // Macros used to mark up functions e.g., __init __exit
#include <linux/module.h>           // Core header for loading LKMs into the kernel
#include <linux/kernel.h>           // Contains types, macros, functions for the kernel

MODULE_LICENSE("GPL");              ///< The license type -- this affects runtime behavior
MODULE_AUTHOR("Moisés Noguera Carrillo");      ///< The author -- visible when you use modinfo
MODULE_DESCRIPTION("Ejemplo de LKM simple para Linux");  ///< The description -- see modinfo
MODULE_VERSION("0.1");              ///< The version of the module

static char *name = "mundo";        ///< An example LKM argument -- default value is "mundo"
module_param(name, charp, S_IRUGO); ///< Param desc. charp = char ptr, S_IRUGO can be read/not changed
MODULE_PARM_DESC(name, "The name to display in /var/log/kern.log");  ///< parameter description

/** @brief The LKM initialization function
 *  The static keyword restricts the visibility of the function to within this C file. The __init
 *  macro means that for a built-in driver (not a LKM) the function is only used at initialization
 *  time and that it can be discarded and its memory freed up after that point.
 *  @return returns 0 if successful
 */
static int __init gandalf_init(void){
   printk(KERN_INFO "Hola %s: Un mago nunca llega tarde, ni pronto, llega exactamente cuándo se lo propone. – Gandalf\n", name);
   return 0;
}

/** @brief The LKM cleanup function
 *  Similar to the initialization function, it is static. The __exit macro notifies that if this
 *  code is used for a built-in driver (not a LKM) that this function is not required.
 */
static void __exit kenobi_exit(void){
   printk(KERN_INFO "Adiós %s: Que la fuerza te acompañe. – Obi-Wan Kenobi\n", name);
}

/** @brief A module must use the module_init() module_exit() macros from linux/init.h, which
 *  identify the initialization function at insertion time and the cleanup function (as
 *  listed above)
 */
module_init(gandalf_init);
module_exit(kenobi_exit);
