from sys import version_info, exit, exc_info
from traceback import print_tb, format_exception_only
from random import choices
from string import ascii_letters


class CheckSum:
	def __init__(self, icmp_type, icmp_code, icmp_id1, icmp_id2, icmp_seq1, icmp_seq2):
	# Add List [リスト作成]
		self.values_list = [icmp_type, icmp_code, icmp_id1, icmp_id2, icmp_seq1, icmp_seq2]

	def t_checksum(self):
		try:
		# Python Version Check [Pythonバージョン確認]
			if version_info.major > 2:
				xrange = range
	
		# Initialization [初期設定]
			checksum_10 = 0
			random_lenght = 32
	
		# Generate 32pieces RandomString [ランダムで32個の文字列を生成]
		# Conversion CharacterValue to UnicodeValue [文字をUnicode値]
		# Add data [dataを追加]
			data = choices(ascii_letters, k=random_lenght)
			data_unicode = [ord(data_char) for data_char in data]
			checksum_list = self.values_list + data_unicode

		# Change FloatType(ex.18.0) > IntType(ex.18) [float型(例.18.0) > int型(例.18)に変更]
		# Add checksum_list[checksum_listを足していく]
			checksum_list_len = int(len(checksum_list)/2)
			for i in xrange(checksum_list_len):
				checksum_10 += (checksum_list[i*2] << 8) | (checksum_list[i*2+1])

		# Get 16bit [16ビットを取得(ex.1101011001010100010 and 1111111111111111 = 1011001010100010)]
		# ShiftRight 16bit Get 17bit or more [右に16ビット移動し、17ビット以上を取得(ex.1101011001010100010 and 1111111111111111 = 0000000000000110)]
		# ReturnValue Decimal [戻り値を10進数]
			checksum_10 = (checksum_10 & 0xffff) + (checksum_10 >> 16)
			checksum = checksum_10 ^ 0xffff
			return checksum, data_unicode
		except KeyboardInterrupt:
			print(f'\n\nProcess Interrupted [処理を中断しました]')
			exit(1)
		except:
		# Get ErrorMessage [エラーメッセージ取得]
			exc_type, exc_message, exc_object = exc_info()
			exc_list = format_exception_only(exc_type, exc_message)
			error_message = ''.join(exc_message for exc_message in exc_list)
			print_tb(exc_object)
			print(f'  {error_message}')
			exit(1)
