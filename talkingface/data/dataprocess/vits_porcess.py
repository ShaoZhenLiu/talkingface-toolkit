import argparse
from talkingface.utils.vits_utils import text
from talkingface.utils.vits_utils.utils import load_filepaths_and_text


def vits_process(config, out_extension="cleaned", text_index=1):
    # filelists = ["filelists/list.txt", "filelists/list_val.txt"]
    text_cleaners = config["text_cleaners"]
    filelists = [config["train_filelist_raw"], config["val_filelist_raw"]]
    for filelist in filelists:
        print("START:", filelist)
        filepaths_and_text = load_filepaths_and_text(filelist)
        for i in range(len(filepaths_and_text)):
            original_text = filepaths_and_text[i][text_index]
            cleaned_text = text._clean_text(original_text, text_cleaners)
            filepaths_and_text[i][text_index] = cleaned_text

        new_filelist = filelist + "." + out_extension
        with open(new_filelist, "w", encoding="utf-8") as f:  # 每次都是清空后从头写入
            f.writelines(["|".join(x) + "\n" for x in filepaths_and_text])


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--out_extension", default="cleaned")
#     parser.add_argument("--text_index", default=1, type=int)
#     parser.add_argument("--filelists", nargs="+", default=["filelists/list.txt", "filelists/list_val.txt"])
#     parser.add_argument("--text_cleaners", nargs="+", default=["cjke_cleaners2"])
#
#     args = parser.parse_args()
#
#     for filelist in args.filelists:
#         print("START:", filelist)
#         filepaths_and_text = load_filepaths_and_text(filelist)
#         for i in range(len(filepaths_and_text)):
#             original_text = filepaths_and_text[i][args.text_index]
#             cleaned_text = text._clean_text(original_text, args.text_cleaners)
#             filepaths_and_text[i][args.text_index] = cleaned_text
#
#         new_filelist = filelist + "." + args.out_extension
#         with open(new_filelist, "w", encoding="utf-8") as f:
#             f.writelines(["|".join(x) + "\n" for x in filepaths_and_text])
