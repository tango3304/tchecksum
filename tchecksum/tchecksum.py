from sys import version_info

class CheckSum:
	def __init__(self, icmp_type, icmp_code, icmp_id1, icmp_id2, icmp_seq1, icmp_seq2, data):
	# Check data Bytes Type [dataがバイト型か確認]
		if type(data) != bytes:
			data = data.encode('UTF-8')

	# Add type, code, id, seq [type, code, id, seqを追加]
		self.checksum_list = [icmp_type, icmp_code, icmp_id1, icmp_id2, icmp_seq1, icmp_seq2]
	
	# Add ByteData [Byte_Dataを追加]
		self.checksum_list.extend(data)
		self.checksum_10 = 0


	def t_checksum(self):
	# Python Version Check [Pythonバージョン確認]
		if version_info.major > 2:
			xrange = range
		
	# Change FloatType(ex.18.0) > IntType(ex.18) [float型(例.18.0) > int型(例.18)に変更]
	# Add checksum_list[checksum_listを足していく]
		checksum_list_len = int(len(self.checksum_list)/2)
		for i in xrange(checksum_list_len):
			self.checksum_10 += (self.checksum_list[i*2] << 8) | (self.checksum_list[i*2+1])

	# Get 16bit [16ビットを取得(ex.1101011001010100010 and 1111111111111111 = 1011001010100010)]
	# ShiftRight 16bit Get 17bit or more [右に16ビット移動し、17ビット以上を取得(ex.1101011001010100010 and 1111111111111111 = 0000000000000110)]
	# ReturnValue Hexadecimal [戻り値を16進数]
		self.checksum_10 = (self.checksum_10 & 0xffff) + (self.checksum_10 >> 16)
		checksum = self.checksum_10 ^ 0xffff
		return hex(checksum)
